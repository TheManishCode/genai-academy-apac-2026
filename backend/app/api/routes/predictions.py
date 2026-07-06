from fastapi import APIRouter

from app.ml.predictor import PredictionEngine
from app.models.schemas import PredictionRequest, PredictionResponse

router = APIRouter()
engine = PredictionEngine()


@router.post("", response_model=PredictionResponse)
async def predict(request: PredictionRequest) -> PredictionResponse:
    return engine.predict(request)
