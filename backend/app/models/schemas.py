from datetime import datetime
from enum import Enum

from pydantic import BaseModel, Field


class UserRole(str, Enum):
    citizen = "citizen"
    government = "government"
    admin = "admin"
    ngo = "ngo"


class RiskType(str, Enum):
    flood = "flood"
    heatwave = "heatwave"
    aqi = "aqi"
    hospital_load = "hospital_load"
    power = "power"
    rainfall = "rainfall"


class WardRisk(BaseModel):
    ward_id: str
    name: str
    lat: float
    lng: float
    flood_risk: float = Field(ge=0, le=1)
    heat_risk: float = Field(ge=0, le=1)
    aqi: int
    rainfall_mm: float
    population_at_risk: int
    confidence: float = Field(ge=0, le=1)
    reasons: list[str]
    recommended_actions: list[str]
    estimated_impact_reduction: float = Field(ge=0, le=1)


class PredictionRequest(BaseModel):
    ward_id: str | None = None
    horizon_hours: int = Field(default=24, ge=1, le=168)
    risk_types: list[RiskType] = Field(default_factory=lambda: [RiskType.flood, RiskType.aqi])


class PredictionResponse(BaseModel):
    generated_at: datetime
    horizon_hours: int
    risks: list[WardRisk]
    shap_factors: list[dict[str, float | str]]
    gpu_benchmark: dict[str, float]


class AssistantRequest(BaseModel):
    question: str
    role: UserRole = UserRole.government
    location: str | None = None
    model: str | None = Field(
        default=None,
        description="Optional NVIDIA NIM model id override, e.g. 'nvidia/llama-3.1-nemotron-70b-instruct'.",
    )


class AssistantResponse(BaseModel):
    answer: str
    confidence: float
    recommended_actions: list[str]
    generated_sql: str
    citations: list[str]


class CitizenReportRequest(BaseModel):
    text: str
    lat: float | None = None
    lng: float | None = None
    media_type: str = "text"


class CitizenReport(BaseModel):
    report_id: str
    disaster_type: str
    severity: str
    urgency: int = Field(ge=1, le=5)
    location: str
    summary: str
    created_at: datetime


class Alert(BaseModel):
    alert_id: str
    title: str
    severity: str
    message: str
    recommended_actions: list[str]
    created_at: datetime
