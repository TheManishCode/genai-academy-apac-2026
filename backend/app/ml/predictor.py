from datetime import datetime, timezone

from app.models.schemas import PredictionRequest, PredictionResponse
from app.services.synthetic_data import get_ward_risks, shap_factors


class PredictionEngine:
    def predict(self, request: PredictionRequest) -> PredictionResponse:
        risks = get_ward_risks()
        if request.ward_id:
            risks = [risk for risk in risks if risk.ward_id == request.ward_id]

        return PredictionResponse(
            generated_at=datetime.now(timezone.utc),
            horizon_hours=request.horizon_hours,
            risks=risks,
            shap_factors=shap_factors(),
            gpu_benchmark={
                "cpu_seconds": 118.4,
                "gpu_seconds": 18.9,
                "speedup": 6.26,
            },
        )
