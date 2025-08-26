import uuid
import random
from typing import Annotated

from fastapi import Header
from passlib.context import CryptContext
import jwt
from jwt.exceptions import InvalidTokenError
from datetime import datetime, timedelta, timezone
from sqlmodel import select
from pydantic import BaseModel
from sqlalchemy.exc import NoResultFound

from app.database.redis_config import get_redis_config
from app.utils.constants import JWT_SECRETS, OTP_TYPE, REDIS_SECRETS
from app.database.core import db_dependency
from app.entities.entities import Student
from app.exceptions import (
    UserAlreadyExistsException,
    UserNotFoundException,
    InvalidUserCredentialsException,
    InvalidOTPReceivedException,
    OTPAlreadyExpiredException,
    InvalidAccessTokenException,
)
from app.utils.send_email import craft_and_send_OTP_mail

JWT_SECRET_KEY = JWT_SECRETS.JWT_SECRET_KEY
JWT_ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_DAYS = 30

bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
redis_config = get_redis_config()


class OTP_MODEL(BaseModel):
    otp: int
    otp_key: str


def user_exists(email: str, db: db_dependency) -> Student | None:
    """Check if user exists in database or not."""
    query = select(Student).where(Student.email == email)
    user = db.exec(query)
    return user.first()


def create_new_student(name: str, email: str, password: str, institution: str, dob: datetime, db: db_dependency):
    """Sign up new student to our platform."""
    if user_exists(email, db):
        raise UserAlreadyExistsException()

    uid = uuid.uuid4().hex

    new_user = Student(
        id=uid, name=name, email=email,
        password=bcrypt_context.hash(password),
        institution=institution,
        date_of_birth=dob.replace(tzinfo=timezone.utc),
    )
    db.add(new_user)
    db.commit()

    token = create_access_token(uid)

    return {"details": "success", "access_token": token}


def login_existing_student(email: str, password: str, db: db_dependency):
    """Log in existing student."""
    user = user_exists(email, db)

    if not user:
        raise UserNotFoundException()

    if not bcrypt_context.verify(password, user.password):
        raise InvalidUserCredentialsException()

    token = create_access_token(user.id)
    return {"access_token": token}


def generate_otp() -> OTP_MODEL:
    """Generates a 6-digit One-Time-Password and save it in Redis database."""
    otp = random.randint(100000, 999999)
    otp_key = f"otp-key_{uuid.uuid4().hex}"
    redis_config.setex(name=otp_key, value=otp, time=timedelta(minutes=3))
    # otp_formatted = " ".join(str(otp).split())
    return OTP_MODEL(otp=otp, otp_key=otp_key)


def send_otp(otp_type: OTP_TYPE, receiver_email: str):
    """Generate an OTP and send that to the user."""
    otp: OTP_MODEL = generate_otp()
    craft_and_send_OTP_mail(otp_type=otp_type, otp=otp.otp, receiver_email=receiver_email)
    return {"otp_key": otp.otp_key}


def validate_otp(otp: int, otp_key: str):
    """Validates the OTP provided by the user with OTP present in Redis database."""
    otp_verify: str = redis_config.get(otp_key)

    if not otp_verify:
        raise OTPAlreadyExpiredException()

    if str(otp).strip() != otp_verify.strip():
        raise InvalidOTPReceivedException()

    return {"details": "success"}


def create_access_token(uid: str) -> str:
    """Generate a new access token from the user id. Token expires after 30 days."""
    payload: dict[str, datetime | str] = {"uid": uid}
    exp_claim = {"exp": datetime.now(tz=timezone.utc) + timedelta(days=30)}
    payload.update(exp_claim)
    token = jwt.encode(payload=payload, algorithm=JWT_ALGORITHM, key=JWT_SECRET_KEY)
    return token


def validate_access_token(token: str, db: db_dependency) -> bool | Student:
    """Validate the access token provided by the user."""
    try:
        payload: dict = jwt.decode(
            jwt=token, key=JWT_SECRET_KEY, algorithms=[JWT_ALGORITHM]
        )
        user_id = payload.get("uid")

        if not user_id:
            return False

        try:
            statement = select(Student).where(Student.id == user_id)
            user = db.exec(statement=statement).one()
            if not user:
                return False

            return user
        except NoResultFound:
            return False

    except InvalidTokenError:
        return False


def validate_token(token: Annotated[str, Header()]):
    user = validate_access_token(token, db=db_dependency)
    if not user:
        raise InvalidAccessTokenException()

    return user
