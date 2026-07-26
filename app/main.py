from fastapi import FastAPI
from app.telemetry import configure_telemetry

from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor

configure_telemetry()

app = FastAPI(
    title="Hello API",
    version="1.0.0"
)

FastAPIInstrumentor.instrument_app(app)


@app.get("/")
async def hello():
    return {
        "message": "Hello Azure!"
    }


@app.get("/health")
async def health():
    return {
        "status": "UP"
    }