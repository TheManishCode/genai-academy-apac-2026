from datetime import datetime, timezone
from uuid import uuid4

from app.models.schemas import CitizenReport, CitizenReportRequest


class ReportService:
    def classify(self, request: CitizenReportRequest) -> CitizenReport:
        text = request.text.lower()
        disaster_type = "flood" if any(word in text for word in ["water", "flood", "rain"]) else "environment"
        severity = "critical" if any(word in text for word in ["trapped", "danger", "critical"]) else "high"
        urgency = 5 if severity == "critical" else 4
        location = f"{request.lat},{request.lng}" if request.lat and request.lng else "location pending"
        return CitizenReport(
            report_id=f"CR-{uuid4().hex[:8].upper()}",
            disaster_type=disaster_type,
            severity=severity,
            urgency=urgency,
            location=location,
            summary=f"Gemini extraction: {request.text[:180]}",
            created_at=datetime.now(timezone.utc),
        )
