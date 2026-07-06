from dataclasses import dataclass


@dataclass(frozen=True)
class RapidsBenchmark:
    task: str
    cpu_seconds: float
    gpu_seconds: float

    @property
    def speedup(self) -> float:
        return round(self.cpu_seconds / self.gpu_seconds, 2)


def benchmark_summary() -> list[RapidsBenchmark]:
    return [
        RapidsBenchmark("cuDF feature engineering", 42.1, 6.8),
        RapidsBenchmark("XGBoost GPU training", 118.4, 18.9),
        RapidsBenchmark("cuML Isolation Forest", 31.6, 5.4),
    ]
