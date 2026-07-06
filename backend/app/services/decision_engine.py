from app.models.schemas import WardRisk


class DecisionEngine:
    """Turns model outputs into operational decisions."""

    def recommend_for_risk(self, risk: WardRisk) -> list[str]:
        actions = list(risk.recommended_actions)
        if risk.flood_risk >= 0.8:
            actions.append("Send evacuation advisory to residents in sub-1.5m elevation blocks")
        if risk.aqi >= 180:
            actions.append("Trigger public health AQI messaging and mask distribution")
        if risk.population_at_risk > 30000:
            actions.append("Assign incident commander and NGO coordination desk")
        return actions

    def impact_summary(self, risks: list[WardRisk]) -> str:
        total_population = sum(risk.population_at_risk for risk in risks)
        average_reduction = sum(risk.estimated_impact_reduction for risk in risks) / max(len(risks), 1)
        return (
            f"Recommended actions cover {total_population:,} people at risk and are estimated "
            f"to reduce impact by {average_reduction:.0%}."
        )
