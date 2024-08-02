from fastapi import HTTPException
from pydantic import BaseModel, validator

from app.service.constants import APPSEC_PRACTICES


class AppSecModelIn(BaseModel):
    key: str

    @validator('key')
    def validate_key(cls, value):
        if value not in APPSEC_PRACTICES:
            raise HTTPException(status_code=400, detail='Key not found')
        return value
