import logging

from tenacity import retry, stop_after_attempt, wait_exponential

from backend.app.models.schemas import AssistantRequest, AssistantResponse
from backend.app.services.decision_engine import DecisionEngine
from backend.app.services.synthetic_data import get_ward_risks

logger = logging.getLogger(__name__)


class GeminiDecisionService:
    def __init__(self, decision_engine: DecisionEngine | None = None) -> None:
        self.decision_engine = decision_engine or DecisionEngine()

    @retry(wait=wait_exponential(multiplier=0.5, min=0.5, max=2), stop=stop_after_attempt(2))
    async def answer(self, request: AssistantRequest) -> AssistantResponse:
        risks = sorted(get_ward_risks(), key=lambda item: item.flood_risk, reverse=True)
        top = risks[0]
        actions = self.decision_engine.recommend_for_risk(top)
        logger.info("Generated deterministic Gemini-style decision answer for role=%s", request.role)
        return AssistantResponse(
            answer=(
                f"{top.name} is the highest priority area for '{request.question}'. "
                f"The risk is driven by {', '.join(top.reasons[:3])}. "
                f"{self.decision_engine.impact_summary(risks)}"
            ),
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
