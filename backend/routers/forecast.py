from fastapi import APIRouter

from schemas.forecast import ForecastQuery
from services.forecast_service import get_annual_forecast, get_monthly_forecast


router = APIRouter(prefix="/forecast", tags=["Forecast"])


@router.get("/monthly")
def monthly_forecast(latitude: float = 22.5726, longitude: float = 78.9629):
    query = ForecastQuery(latitude=latitude, longitude=longitude)
    return get_monthly_forecast(query)


@router.get("/annual")
def annual_forecast(latitude: float = 22.5726, longitude: float = 78.9629):
    query = ForecastQuery(latitude=latitude, longitude=longitude)
    return get_annual_forecast(query)
