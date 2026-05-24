from fastapi import FastAPI

from app.core.database import Base
from app.core.database import engine

from app.models.security_log import SecurityLog


Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="SentinelAI SOC Platform",
    version="1.0.0"
)


@app.get("/")
async def root():
    return {
        "message": "SOC AI Platform Running"
    }