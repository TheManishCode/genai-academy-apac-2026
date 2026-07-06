from fastapi import APIRouter, File, Form, UploadFile

from backend.app.models.schemas import CitizenReport, CitizenReportRequest
from backend.app.services.report_service import ReportService

router = APIRouter()
service = ReportService()


@router.post("", response_model=CitizenReport)
async def create_report(payload: CitizenReportRequest) -> CitizenReport:
    return service.classify(payload)


@router.post("/upload", response_model=CitizenReport)
async def upload_report(
    file: UploadFile = File(...),
    description: str = Form(default=""),
    lat: float | None = Form(default=None),
    lng: float | None = Form(default=None),
) -> CitizenReport:
    request = CitizenReportRequest(
        text=description or f"Uploaded {file.filename}",
        lat=lat,
        lng=lng,
        media_type=file.content_type or "application/octet-stream",
    )
    return service.classify(request)
