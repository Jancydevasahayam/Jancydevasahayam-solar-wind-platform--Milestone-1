from math import cos, radians

from schemas.forecast import AnnualForecastResponse, ForecastQuery, MonthlyForecastPoint
from services.suitability_service import derive_environmental_data


MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
SOLAR_SEASONALITY = [0.88, 0.96, 1.08, 1.16, 1.2, 1.06, 0.92, 0.9, 0.98, 1.08, 1.02, 0.9]
WIND_SEASONALITY = [0.96, 0.94, 0.98, 1.04, 1.1, 1.18, 1.24, 1.2, 1.08, 1.0, 0.95, 0.93]


def get_monthly_forecast(query: ForecastQuery) -> list[MonthlyForecastPoint]:
    environmental = derive_environmental_data(query.latitude, query.longitude)
    latitude_modifier = 0.9 + (cos(radians(query.latitude)) * 0.18)
    solar_base = environmental.solar_irradiance * 82 * latitude_modifier
    wind_base = environmental.wind_speed * 54

    forecast = []
    for index, month in enumerate(MONTHS):
        solar = round(solar_base * SOLAR_SEASONALITY[index])
        wind = round(wind_base * WIND_SEASONALITY[index])
        forecast.append(MonthlyForecastPoint(month=month, solar=solar, wind=wind, energy=solar + wind))
    return forecast


def get_annual_forecast(query: ForecastQuery) -> AnnualForecastResponse:
    monthly = get_monthly_forecast(query)
    annual_solar = sum(point.solar for point in monthly)
    annual_wind = sum(point.wind for point in monthly)
    return AnnualForecastResponse(
        latitude=query.latitude,
        longitude=query.longitude,
        annual_solar=annual_solar,
        annual_wind=annual_wind,
        annual_energy=annual_solar + annual_wind,
    )
