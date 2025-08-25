from pydantic import BaseModel, EmailStr, AfterValidator, Field
from datetime import datetime, timezone
from fastapi import HTTPException, status
from typing import Annotated
from app.utils.helper import get_age_from_dob


class AuthBaseModel(BaseModel):
    email: EmailStr
    password: str


def dob_not_fake(dob: datetime):
    if get_age_from_dob(datetime.now(timezone.utc), dob) <= 3:
        raise HTTPException(detail="Date of birth must be greater than 3 years.", status_code=status.HTTP_403_FORBIDDEN)
    return dob


class SignUpUserModel(AuthBaseModel):
    name: str
    institution: str = None
    date_of_birth: Annotated[datetime, AfterValidator(dob_not_fake)] = Field(default=None,
                                                                             description="Date of birth must be greater than 3 years.")


class LoginInUserModel(AuthBaseModel):
    pass


class VerifyOtpModel(BaseModel):
    otp: int
    otp_key: str
