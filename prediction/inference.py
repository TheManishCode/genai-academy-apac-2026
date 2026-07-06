from backend.app.ml.predictor import PredictionEngine
from backend.app.models.schemas import PredictionRequest, RiskType


def run_demo_inference() -> None:
    engine = PredictionEngine()
    response = engine.predict(PredictionRequest(horizon_hours=24, risk_types=[RiskType.flood, RiskType.aqi]))
    for risk in response.risks:
        print(risk.name, risk.flood_risk, risk.recommended_actions[0])


if __name__ == "__main__":
    run_demo_inference()
