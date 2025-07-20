from pydantic import BaseModel


class AuthBaseModel(BaseModel):
    email: str
    password: str


class SignUpUserModel(AuthBaseModel):
    name: str


class LoginInUserModel(AuthBaseModel):
    pass


class VerifyOtpModel(BaseModel):
    otp: int
    otp_key: str
