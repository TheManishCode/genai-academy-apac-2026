from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes import alerts, assistant, health, predictions, reports, risks
from app.core.config import settings
from app.core.logging import configure_logging

configure_logging()

app = FastAPI(
    title="EcoMind AI API",
    description="AI Decision Intelligence Platform for Climate Resilience & Disaster Preparedness.",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health.router, prefix="/api/v1", tags=["health"])
app.include_router(risks.router, prefix="/api/v1/risks", tags=["risks"])
app.include_router(predictions.router, prefix="/api/v1/predictions", tags=["predictions"])
app.include_router(assistant.router, prefix="/api/v1/assistant", tags=["assistant"])
app.include_router(reports.router, prefix="/api/v1/reports", tags=["reports"])
app.include_router(alerts.router, prefix="/api/v1/alerts", tags=["alerts"])
