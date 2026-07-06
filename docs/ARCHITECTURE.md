# Architecture

## System Design

```mermaid
flowchart LR
  subgraph Sources
    W[Weather APIs]
    A[AQI APIs]
    S[Satellite and flood feeds]
    C[Citizen reports]
    H[Hospitals and shelters]
  end
  subgraph GoogleCloud[Google Cloud]
    GCS[Cloud Storage raw zone]
    BQ[BigQuery analytics warehouse]
    VX[Vertex AI Gemini]
    RUN[Cloud Run FastAPI]
    FB[Firebase Auth]
  end
  subgraph NVIDIA[NVIDIA GPU Layer]
    CUDF[cuDF preprocessing]
    CUML[cuML anomaly detection]
    XGB[XGBoost GPU forecasting]
  end
  subgraph Product
    API[Decision APIs]
    UI[React dashboard]
  end
  Sources --> GCS --> BQ --> CUDF --> CUML --> XGB --> API
  BQ --> VX --> API
  FB --> UI
  API --> UI
```

## Decision Intelligence Loop

1. Collect raw climate, environmental, infrastructure and citizen signals.
2. Clean and enrich features with geospatial, temporal and infrastructure context.
3. Predict risks across flood, AQI, heatwave, emergency demand and hospital load.
4. Explain predictions with SHAP-style factor ranking.
5. Generate actions through the decision engine and Gemini.
6. Present actions, confidence, tradeoffs and estimated impact reduction.

## ER Diagram

```mermaid
erDiagram
  WARD ||--o{ RISK_FORECAST : has
  WARD ||--o{ CITIZEN_REPORT : receives
  WARD ||--o{ RESOURCE : contains
  RISK_FORECAST ||--o{ RECOMMENDATION : generates
  ALERT ||--o{ RECOMMENDATION : includes
  USER ||--o{ CITIZEN_REPORT : submits

  WARD {
    string ward_id PK
    string name
    float lat
    float lng
    int population
  }
  RISK_FORECAST {
    string forecast_id PK
    string ward_id FK
    string risk_type
    float risk_score
    float confidence
    timestamp horizon
  }
  CITIZEN_REPORT {
    string report_id PK
    string ward_id FK
    string media_type
    string severity
    int urgency
  }
  RESOURCE {
    string resource_id PK
    string ward_id FK
    string resource_type
    int capacity
  }
  RECOMMENDATION {
    string recommendation_id PK
    string action
    float estimated_impact_reduction
  }
```
