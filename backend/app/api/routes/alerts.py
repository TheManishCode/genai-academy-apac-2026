from datetime import datetime, timezone

from fastapi import APIRouter

from app.models.schemas import Alert

router = APIRouter()


@router.get("", response_model=list[Alert])
async def list_alerts() -> list[Alert]:
    now = datetime.now(timezone.utc)
    return [
        Alert(
            alert_id="AL-RAIN-001",
            title="Heavy rainfall threshold breached",
            severity="critical",
            message="3 river-adjacent wards need pump staging before 02:00.",
            recommended_actions=["Stage pumps", "Open shelters", "Close vulnerable underpasses"],
            created_at=now,
        ),
        Alert(
            alert_id="AL-AQI-008",
            title="AQI health advisory",
            severity="high",
            message="Industrial ward PM2.5 is projected to remain unhealthy for 18 hours.",
            recommended_actions=["Reduce outdoor shifts", "Deploy health vans", "Notify schools"],
            created_at=now,
        ),
    ]
