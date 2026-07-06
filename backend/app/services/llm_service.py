import logging

from app.models.schemas import AssistantRequest, AssistantResponse, WardRisk
from app.rag.pipeline import RAGPipeline
from app.services.decision_engine import DecisionEngine
from app.services.nim_client import NIMClient, NIMClientError
from app.services.synthetic_data import get_ward_risks

logger = logging.getLogger(__name__)


class LLMDecisionService:
    """Generates decision-assistant answers grounded in ward risk forecasts.

    NVIDIA NIM (see [[nim_client]]) is the base model provider: when
    NVIDIA_NIM_API_KEY is configured, the question and retrieved risk context
    are sent to the configured (or request-selected) NIM model. If NIM is not
    configured or the call fails, a deterministic answer built from the
    decision engine is used instead so the assistant still works offline.
    """

    def __init__(
        self,
        decision_engine: DecisionEngine | None = None,
        rag: RAGPipeline | None = None,
        nim_client: NIMClient | None = None,
    ) -> None:
        self.decision_engine = decision_engine or DecisionEngine()
        self.rag = rag or RAGPipeline()
        self.nim_client = nim_client or NIMClient()

    async def answer(self, request: AssistantRequest) -> AssistantResponse:
        risks = sorted(get_ward_risks(), key=lambda item: item.flood_risk, reverse=True)
        top = risks[0]
        actions = self.decision_engine.recommend_for_risk(top)

        answer_text = await self._generate_answer(request, risks, top, actions)

        return AssistantResponse(
            answer=answer_text,
            confidence=top.confidence,
            recommended_actions=actions,
            generated_sql=(
                "SELECT ward_id, name, flood_risk, aqi, population_at_risk "
                "FROM `ecomind.risk_forecasts` "
                "WHERE forecast_horizon_hours = 24 "
                "ORDER BY flood_risk DESC LIMIT 5"
            ),
            citations=[
                "BigQuery:ecomind.risk_forecasts",
                "OpenAQ latest station readings",
                "Synthetic citizen-report stream",
            ],
        )

    async def _generate_answer(
        self,
        request: AssistantRequest,
        risks: list[WardRisk],
        top: WardRisk,
        actions: list[str],
    ) -> str:
        if self.nim_client.is_configured:
            try:
                system_prompt = (
                    "You are EcoMind AI, a climate resilience decision assistant. "
                    "Be concise, stay grounded in the provided context, and reference "
                    "concrete risk drivers and actions."
                )
                user_prompt = (
                    f"{self.rag.build_prompt(request.question)}\n\n"
                    f"Requesting role: {request.role.value}\n"
                    f"Highest-priority ward: {top.name} (flood_risk={top.flood_risk:.2f}, "
                    f"aqi={top.aqi}, population_at_risk={top.population_at_risk}).\n"
                    f"Decision-engine recommended actions: {', '.join(actions)}.\n"
                    "Write a 2-4 sentence answer for the operator."
                )
                return await self.nim_client.chat(system_prompt, user_prompt, model=request.model)
            except NIMClientError as exc:
                logger.warning("NVIDIA NIM call failed, using deterministic fallback: %s", exc)

        logger.info("Generated deterministic fallback decision answer for role=%s", request.role)
        return (
            f"{top.name} is the highest priority area for '{request.question}'. "
            f"The risk is driven by {', '.join(top.reasons[:3])}. "
            f"{self.decision_engine.impact_summary(risks)}"
        )
