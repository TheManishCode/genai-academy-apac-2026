import logging

import httpx
from tenacity import retry, retry_if_exception_type, stop_after_attempt, wait_exponential

from app.core.config import settings

logger = logging.getLogger(__name__)


class NIMClientError(RuntimeError):
    """Raised when the NVIDIA NIM API cannot produce a usable completion.

    Not retried: a bad/missing API key or malformed request won't succeed on
    retry, so failing fast keeps the deterministic fallback path fast too.
    """


class TransientNIMError(NIMClientError):
    """Raised for retryable failures: timeouts, connection errors, 5xx responses."""


class NIMClient:
    """Async client for NVIDIA NIM's OpenAI-compatible chat completions API.

    NIM hosts many swappable models (Llama, Nemotron, Mixtral, Gemma, ...) behind
    one endpoint and API key, so switching models is just changing the `model`
    field on the request rather than pointing at a different provider/SDK.
    """

    def __init__(self) -> None:
        self.base_url = settings.nvidia_nim_base_url
        self.default_model = settings.nvidia_nim_model
        self.available_models = settings.nvidia_nim_models

    @property
    def is_configured(self) -> bool:
        return bool(settings.nvidia_nim_api_key)

    def resolve_model(self, requested_model: str | None) -> str:
        if requested_model and requested_model in self.available_models:
            return requested_model
        return self.default_model

    @retry(
        wait=wait_exponential(multiplier=0.5, min=0.5, max=4),
        stop=stop_after_attempt(3),
        retry=retry_if_exception_type(TransientNIMError),
        reraise=True,
    )
    async def chat(self, system_prompt: str, user_prompt: str, model: str | None = None) -> str:
        if not self.is_configured:
            raise NIMClientError("NVIDIA_NIM_API_KEY is not set")

        resolved_model = self.resolve_model(model)
        payload = {
            "model": resolved_model,
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            "temperature": settings.nvidia_nim_temperature,
            "max_tokens": settings.nvidia_nim_max_tokens,
        }
        headers = {
            "Authorization": f"Bearer {settings.nvidia_nim_api_key}",
            "Content-Type": "application/json",
        }

        try:
            async with httpx.AsyncClient(base_url=self.base_url, timeout=20.0) as client:
                response = await client.post("/chat/completions", json=payload, headers=headers)
                response.raise_for_status()
                data = response.json()
        except httpx.HTTPStatusError as exc:
            message = f"NVIDIA NIM request failed for model={resolved_model}: {exc}"
            if exc.response.status_code >= 500:
                raise TransientNIMError(message) from exc
            raise NIMClientError(message) from exc
        except (httpx.TimeoutException, httpx.TransportError) as exc:
            raise TransientNIMError(f"NVIDIA NIM request failed for model={resolved_model}: {exc}") from exc

        try:
            return data["choices"][0]["message"]["content"].strip()
        except (KeyError, IndexError, TypeError) as exc:
            raise NIMClientError("Unexpected NVIDIA NIM response shape") from exc
