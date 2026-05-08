from fastapi import FastAPI

app = FastAPI(
    title="SentinelAI SOC Platform",
    version="1.0.0"
)

@app.get("/")
async def root():
    return {
        "message": "SOC AI Platform Running"
    }