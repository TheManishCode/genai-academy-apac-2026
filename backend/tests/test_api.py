from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_health() -> None:
    response = client.get("/api/v1/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_prediction_returns_risks() -> None:
    response = client.post("/api/v1/predictions", json={"horizon_hours": 24, "risk_types": ["flood"]})
    assert response.status_code == 200
    payload = response.json()
    assert payload["risks"]
    assert payload["gpu_benchmark"]["speedup"] > 1


def test_assistant_returns_recommendations() -> None:
    response = client.post(
        "/api/v1/assistant/ask",
        json={"question": "Which wards are likely to flood tomorrow?", "role": "government"},
    )
    assert response.status_code == 200
    payload = response.json()
    assert payload["recommended_actions"]
    assert "SELECT" in payload["generated_sql"]
