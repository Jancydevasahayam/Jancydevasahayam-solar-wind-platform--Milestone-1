from schemas.forecast import ForecastQuery
from services.forecast_service import get_monthly_forecast
from services.suitability_service import get_recent_analyses


def get_dashboard_summary() -> dict:
    analyses = get_recent_analyses()
    total_sites = len(analyses)
    suitable_sites = len([item for item in analyses if item["overall_score"] >= 65])
    average_solar = round(sum(item["solar_score"] for item in analyses) / total_sites)
    average_wind = round(sum(item["wind_score"] for item in analyses) / total_sites)
    overall = round(sum(item["overall_score"] for item in analyses) / total_sites)
    forecast = get_monthly_forecast(ForecastQuery(latitude=analyses[0]["latitude"], longitude=analyses[0]["longitude"]))

    return {
        "cards": {
            "total_sites": total_sites,
            "suitable_sites": suitable_sites,
            "average_solar_score": average_solar,
            "average_wind_score": average_wind,
            "overall_suitability": overall,
        },
        "environmental_summary": analyses[0]["environmental_summary"],
        "forecast": [point.model_dump() for point in forecast],
        "recent_analysis": analyses,
    }
