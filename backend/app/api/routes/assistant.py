from fastapi import APIRouter

from app.models.schemas import AssistantRequest, AssistantResponse
from app.services.llm_service import LLMDecisionService

router = APIRouter()
service = LLMDecisionService()


@router.post("/ask", response_model=AssistantResponse)
async def ask(request: AssistantRequest) -> AssistantResponse:
    return await service.answer(request)


@router.get("/models")
async def list_models() -> dict[str, str | list[str]]:
    client = service.nim_client
    return {
        "provider": "nvidia_nim",
        "default_model": client.default_model,
        "available_models": client.available_models,
    }
