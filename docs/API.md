# API Documentation

Base URL: `/api/v1`

## Health

`GET /health`

Returns service status and active environment.

## Risks

`GET /risks`

Returns current ward-level risk features, explanations and recommended actions.

## Predictions

`POST /predictions`

```json
{
  "ward_id": "W-14",
  "horizon_hours": 24,
  "risk_types": ["flood", "aqi"]
}
```

Returns ward risks, SHAP factors and CPU/GPU benchmark metadata.

## Assistant

`POST /assistant/ask`

```json
{
  "question": "Which wards are likely to flood tomorrow?",
  "role": "government",
  "location": "Delhi"
}
```

Returns natural language answer, confidence, generated SQL, citations and recommended actions.

## Citizen Reports

`POST /reports`

```json
{
  "text": "Water is rising near the underpass and traffic is blocked.",
  "lat": 28.621,
  "lng": 77.256,
  "media_type": "text"
}
```

`POST /reports/upload` supports `multipart/form-data` for image, video or audio.

## Alerts

`GET /alerts`

Returns active alerts with severity and recommended actions.
