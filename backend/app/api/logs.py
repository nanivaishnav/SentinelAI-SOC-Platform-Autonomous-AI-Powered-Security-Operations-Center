from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.core.deps import get_db

from app.models.security_log import SecurityLog

from app.schemas.security_log import SecurityLogCreate


router = APIRouter()


@router.post("/ingest")

async def ingest_log(
    payload: SecurityLogCreate,
    db: Session = Depends(get_db)
):

    new_log = SecurityLog(

        source=payload.source,

        event_type=payload.event_type,

        severity=payload.severity,

        raw_log=payload.raw_log
    )

    db.add(new_log)

    db.commit()

    db.refresh(new_log)

    return {

        "message": "Log ingested successfully",

        "log_id": new_log.id
    }