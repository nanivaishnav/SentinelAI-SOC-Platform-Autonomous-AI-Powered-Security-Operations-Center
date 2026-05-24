from pydantic import BaseModel
from typing import Optional
from typing import Dict
from typing import Any


class SecurityLogCreate(BaseModel):

    source: str

    event_type: str

    severity: Optional[str] = "low"

    raw_log: Dict[str, Any]