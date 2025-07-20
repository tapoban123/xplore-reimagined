from fastapi import APIRouter
from pydantic import EmailStr

from app.database.core import db_dependency
from .services import create_new_student, login_existing_student, send_otp, validate_otp
from .models import SignUpUserModel, LoginInUserModel, VerifyOtpModel
from app.utils.constants import OTP_TYPE

student_auth_router = APIRouter(
    prefix="/student/auth",
    tags=["Auth"],
)


@student_auth_router.post("/sign-up")
def sign_up_student(user_details: SignUpUserModel, db: db_dependency):
    return create_new_student(
        name=user_details.name,
        email=user_details.email,
        password=user_details.password,
        db=db,
    )


@student_auth_router.post("/log-in")
def login_in_student(user_details: LoginInUserModel, db: db_dependency):
    return login_existing_student(
        email=user_details.email, password=user_details.password, db=db
    )


@student_auth_router.post("/send-log-in-otp")
def send_sign_in_otp(receiver_email: EmailStr):
    return send_otp(otp_type=OTP_TYPE.SIGN_IN, receiver_email=str(receiver_email))


@student_auth_router.post("/send-sign-up-otp")
def send_sign_up_otp(receiver_email: EmailStr):
    return send_otp(otp_type=OTP_TYPE.SIGN_UP, receiver_email=str(receiver_email))


@student_auth_router.post("/send-reset-password-otp")
def send_reset_password_otp(receiver_email: EmailStr):
    return send_otp(
        otp_type=OTP_TYPE.RESET_PASSWORD, receiver_email=str(receiver_email)
    )


@student_auth_router.post("/verify-otp")
def verify_otp(otp: VerifyOtpModel):
    return validate_otp(otp_key=otp.otp_key, otp=otp.otp)
