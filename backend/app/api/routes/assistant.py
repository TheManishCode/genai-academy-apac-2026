from fastapi import APIRouter

from backend.app.models.schemas import AssistantRequest, AssistantResponse
from backend.app.services.gemini_service import GeminiDecisionService

router = APIRouter()
service = GeminiDecisionService()


@router.post("/ask", response_model=AssistantResponse)
async def ask(request: AssistantRequest) -> AssistantResponse:
    return await service.answer(request)
