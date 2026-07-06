from dataclasses import dataclass


@dataclass(frozen=True)
class RetrievedContext:
    source: str
    text: str
    score: float


class RAGPipeline:
    def retrieve(self, question: str) -> list[RetrievedContext]:
        del question
        return [
            RetrievedContext(
                source="BigQuery:ecomind.risk_forecasts",
                text="Ward-level 24h forecasts with flood, AQI, heat and hospital demand risk.",
                score=0.91,
            ),
            RetrievedContext(
                source="GCS:citizen-reports/latest",
                text="Recent citizen reports mention waterlogging, road closures and stranded vehicles.",
                score=0.84,
            ),
        ]

    def build_prompt(self, question: str) -> str:
        context = "\n".join(f"- {item.source}: {item.text}" for item in self.retrieve(question))
        return (
            "You are EcoMind AI, a climate resilience decision assistant. "
            "Answer with risks, reasons, actions, confidence, and SQL when useful.\n\n"
            f"Question: {question}\nContext:\n{context}"
        )
