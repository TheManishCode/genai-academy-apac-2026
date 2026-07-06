from fastapi import APIRouter

from backend.app.models.schemas import WardRisk
from backend.app.services.synthetic_data import get_ward_risks

router = APIRouter()


@router.get("", response_model=list[WardRisk])
async def list_risks() -> list[WardRisk]:
    return get_ward_risks()
