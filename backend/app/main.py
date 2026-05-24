from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy import JSON

from datetime import datetime

from app.core.database import Base


class SecurityLog(Base):

    __tablename__ = "security_logs"

    id = Column(Integer, primary_key=True, index=True)

    source = Column(String)
    event_type = Column(String)
    severity = Column(String, default="low")

    raw_log = Column(JSON)

    created_at = Column(DateTime, default=datetime.utcnow)