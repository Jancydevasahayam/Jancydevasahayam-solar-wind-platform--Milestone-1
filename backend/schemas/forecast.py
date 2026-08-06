from pydantic import BaseModel, Field


class ForecastQuery(BaseModel):
    latitude: float = Field(..., ge=-90, le=90)
    longitude: float = Field(..., ge=-180, le=180)


class MonthlyForecastPoint(BaseModel):
    month: str
    solar: int
    wind: int
    energy: int


class AnnualForecastResponse(BaseModel):
    latitude: float
    longitude: float
    annual_solar: int
    annual_wind: int
    annual_energy: int
    unit: str = "MWh"
