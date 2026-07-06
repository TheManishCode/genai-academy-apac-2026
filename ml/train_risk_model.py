"""Train a local flood-risk baseline.

Production deployment can replace pandas/sklearn with cuDF, cuML and XGBoost GPU.
"""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split


def make_dataset(rows: int = 1200) -> tuple[np.ndarray, np.ndarray]:
    rng = np.random.default_rng(42)
    rainfall = rng.normal(85, 35, rows).clip(0, 220)
    river_level = rng.normal(0.55, 0.2, rows).clip(0, 1)
    drain_complaints = rng.poisson(8, rows)
    elevation = rng.normal(7, 2, rows).clip(1, 14)
    pump_availability = rng.normal(0.65, 0.2, rows).clip(0, 1)
    features = np.column_stack([rainfall, river_level, drain_complaints, elevation, pump_availability])
    target = (
        0.003 * rainfall
        + 0.34 * river_level
        + 0.018 * drain_complaints
        - 0.035 * elevation
        - 0.18 * pump_availability
        + rng.normal(0, 0.04, rows)
    ).clip(0, 1)
    return features, target


def main() -> None:
    features, target = make_dataset()
    x_train, x_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)
    model = RandomForestRegressor(n_estimators=120, random_state=42)
    model.fit(x_train, y_train)
    predictions = model.predict(x_test).clip(0, 1)
    metrics = {"mae": round(float(mean_absolute_error(y_test, predictions)), 4)}
    Path("models").mkdir(exist_ok=True)
    Path("models/risk_model_metrics.json").write_text(json.dumps(metrics, indent=2), encoding="utf-8")
    print(metrics)


if __name__ == "__main__":
    main()
