from backend.app.models.schemas import WardRisk


def get_ward_risks() -> list[WardRisk]:
    return [
        WardRisk(
            ward_id="W-14",
            name="Yamuna Bank",
            lat=28.621,
            lng=77.256,
            flood_risk=0.91,
            heat_risk=0.42,
            aqi=181,
            rainfall_mm=138,
            population_at_risk=42000,
            confidence=0.87,
            reasons=["River level anomaly", "Saturated soil index", "Blocked drains", "High rainfall forecast"],
            recommended_actions=[
                "Pre-stage 18 pumps",
                "Open 5 shelters",
                "Close low-lying underpasses",
                "Notify hospitals within 6 km",
            ],
            estimated_impact_reduction=0.34,
        ),
        WardRisk(
            ward_id="W-22",
            name="Civil Lines",
            lat=28.681,
            lng=77.225,
            flood_risk=0.74,
            heat_risk=0.51,
            aqi=154,
            rainfall_mm=102,
            population_at_risk=28000,
            confidence=0.82,
            reasons=["Drainage complaints up 2.4x", "Low road elevation", "Pump availability delayed"],
            recommended_actions=[
                "Dispatch drain clearance crews",
                "Divert Ring Road traffic",
                "Prepare two relief schools",
            ],
            estimated_impact_reduction=0.27,
        ),
        WardRisk(
            ward_id="W-09",
            name="Okhla Industrial",
            lat=28.535,
            lng=77.283,
            flood_risk=0.58,
            heat_risk=0.68,
            aqi=211,
            rainfall_mm=81,
            population_at_risk=19000,
            confidence=0.79,
            reasons=["Industrial PM2.5 spike", "Stagnant wind", "Night-time heat retention"],
            recommended_actions=[
                "Issue AQI advisory",
                "Reduce outdoor shifts",
                "Deploy mobile health vans",
            ],
            estimated_impact_reduction=0.22,
        ),
    ]


def shap_factors() -> list[dict[str, float | str]]:
    return [
        {"factor": "Rain forecast", "impact": 0.32},
        {"factor": "Drain complaints", "impact": 0.24},
        {"factor": "River level", "impact": 0.18},
        {"factor": "Road elevation", "impact": 0.14},
        {"factor": "Pump availability", "impact": 0.12},
    ]
