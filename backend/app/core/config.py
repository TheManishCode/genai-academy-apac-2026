from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_env: str = "development"
    google_cloud_project: str = "demo-project"
    google_cloud_location: str = "us-central1"
    bigquery_dataset: str = "ecomind"
    gcs_bucket: str = "ecomind-ai-data"
    vertex_model: str = "gemini-2.5-pro"
    gemini_api_key: str | None = None
    cors_origins_raw: str = Field(
        default="http://localhost:5173,http://127.0.0.1:5173",
        alias="CORS_ORIGINS",
    )

    # NVIDIA NIM is the base LLM provider for the decision assistant. NIM exposes
    # an OpenAI-compatible /chat/completions endpoint that can serve many models
    # (Llama, Nemotron, Mixtral, Gemma, ...), so "model switching" is just picking
    # a different `model` id against the same endpoint/key.
    llm_provider: str = "nvidia_nim"
    nvidia_nim_api_key: str | None = None
    nvidia_nim_base_url: str = "https://integrate.api.nvidia.com/v1"
    nvidia_nim_model: str = "meta/llama-3.1-70b-instruct"
    nvidia_nim_models_raw: str = Field(
        default=(
            "meta/llama-3.1-70b-instruct,"
            "nvidia/llama-3.1-nemotron-70b-instruct,"
            "mistralai/mixtral-8x22b-instruct-v0.1,"
            "google/gemma-2-27b-it"
        ),
        alias="NVIDIA_NIM_MODELS",
    )
    nvidia_nim_temperature: float = 0.4
    nvidia_nim_max_tokens: int = 512

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

    @property
    def cors_origins(self) -> list[str]:
        return [origin.strip() for origin in self.cors_origins_raw.split(",") if origin.strip()]

    @property
    def nvidia_nim_models(self) -> list[str]:
        return [model.strip() for model in self.nvidia_nim_models_raw.split(",") if model.strip()]


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
