from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers import dashboard, forecast, suitability


app = FastAPI(title="Solar & Wind Deployment Intelligence Platform - Milestone 3")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://127.0.0.1:3000",
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(dashboard.router)
app.include_router(suitability.router)
app.include_router(forecast.router)


@app.get("/")
def root():
    return {"message": "Milestone 3 Renewable Energy Intelligence API is running"}
