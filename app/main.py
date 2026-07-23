from fastapi import FastAPI

app = FastAPI(
    title="Hello API",
    version="1.0.0"
)


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