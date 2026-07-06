CREATE SCHEMA IF NOT EXISTS `ecomind`;

CREATE TABLE IF NOT EXISTS `ecomind.wards` (
  ward_id STRING NOT NULL,
  name STRING NOT NULL,
  lat FLOAT64,
  lng FLOAT64,
  population INT64
);

CREATE TABLE IF NOT EXISTS `ecomind.risk_forecasts` (
  forecast_id STRING NOT NULL,
  ward_id STRING NOT NULL,
  risk_type STRING NOT NULL,
  risk_score FLOAT64,
  confidence FLOAT64,
  forecast_horizon_hours INT64,
  generated_at TIMESTAMP
);

CREATE TABLE IF NOT EXISTS `ecomind.citizen_reports` (
  report_id STRING NOT NULL,
  ward_id STRING,
  media_uri STRING,
  disaster_type STRING,
  severity STRING,
  urgency INT64,
  extracted_summary STRING,
  created_at TIMESTAMP
);
