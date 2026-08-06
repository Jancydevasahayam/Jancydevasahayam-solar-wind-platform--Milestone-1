from fastapi import APIRouter

from schemas.suitability import SuitabilityAnalyzeRequest, SuitabilityAnalyzeResponse
from services.suitability_service import analyze_site_suitability


router = APIRouter(prefix="/suitability", tags=["Site Suitability"])


@router.post("/analyze", response_model=SuitabilityAnalyzeResponse)
def analyze_suitability(payload: SuitabilityAnalyzeRequest):
    return analyze_site_suitability(payload)
