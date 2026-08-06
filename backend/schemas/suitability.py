from pydantic import BaseModel, Field


class EnvironmentalInputs(BaseModel):
    solar_irradiance: float | None = Field(default=None, ge=0, description="kWh/m2/day")
    wind_speed: float | None = Field(default=None, ge=0, description="m/s")
    temperature: float | None = Field(default=None, description="Celsius")
    rainfall: float | None = Field(default=None, ge=0, description="mm/month")
    elevation: float | None = Field(default=None, ge=0, description="meters")
    land_slope: float | None = Field(default=None, ge=0, description="degrees")


class SuitabilityAnalyzeRequest(BaseModel):
    latitude: float = Field(..., ge=-90, le=90)
    longitude: float = Field(..., ge=-180, le=180)
    environmental_data: EnvironmentalInputs | None = None


class DeploymentRecommendation(BaseModel):
    recommendation: str
    reason: str
    confidence: int


class EnvironmentalSummary(BaseModel):
    solar_irradiance: float
    wind_speed: float
    temperature: float
    rainfall: float
    elevation: float
    land_slope: float


class SuitabilityAnalyzeResponse(BaseModel):
    latitude: float
    longitude: float
    overall_score: int
    solar_score: int
    wind_score: int
    category: str
    recommendation: DeploymentRecommendation
    environmental_summary: EnvironmentalSummary
