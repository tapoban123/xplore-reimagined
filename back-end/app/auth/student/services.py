import uuid
import random

from passlib.context import CryptContext
import jwt
from jwt.exceptions import InvalidTokenError
from datetime import datetime, timedelta, timezone
from sqlmodel import select

from app.utils.constants import JWT_SECRETS, OTP_TYPE
from app.database.core import db_dependency
from app.entities.students import Student
from app.exceptions import UserAlreadyExistsException, UserNotFoundException, InvalidUserCredentialsException
from app.utils.send_email import send_mail

JWT_SECRET_KEY = JWT_SECRETS.JWT_SECRET_KEY
JWT_ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_DAYS = 30

bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def user_exists(email: str, db: db_dependency) -> Student | None:
    query = select(Student).where(Student.email == email)
    user = db.exec(query)
    return user.first()


def create_new_student(name: str, email: str, password: str, db: db_dependency):
    """Function to sign up new students to our platform."""
    if user_exists(email, db):
        raise UserAlreadyExistsException()

    uid = uuid.uuid4().hex

    new_user = Student(
        id=uid,
        name=name,
        email=email,
        password=bcrypt_context.hash(password)
    )
    db.add(new_user)
    db.commit()

    token = create_access_token(uid)

    return {"details": "success", "access_token": token}


def login_existing_student(email: str, password: str, db: db_dependency):
    """Function that logs in existing student."""
    user = user_exists(email, db)

    if not user:
        raise UserNotFoundException()

    if not bcrypt_context.verify(password, user.password):
        raise InvalidUserCredentialsException()

    token = create_access_token(user.id)

    return {"access_token": token}


def generate_otp() -> str:
    """Function that generates a 6-digit One-Time-Password."""
    otp = random.randint(100000, 999999)
    otp_formatted = " ".join(str(otp).split())
    return otp_formatted


def send_otp(otp_type: OTP_TYPE, receiver_email: str):
    """Function that generates an OTP and sends that to the user."""
    otp: str = generate_otp()
    send_mail(otp_type=otp_type, otp=otp, receiver_email=receiver_email)
    return {"details": "success"}


def validate_otp(otp: str, otp_key: str):
    """Function that validates the provided OTP."""
    pass


def create_access_token(uid: str) -> str:
    """Function that generates a new access token from the user id. Token expires after 30 days."""
    payload: dict[str, datetime | str] = {"uid": uid}
    exp_claim = {"exp": datetime.now(tz=timezone.utc) + timedelta(days=30)}
    payload.update(exp_claim)
    token = jwt.encode(payload=payload, algorithm=JWT_ALGORITHM, key=JWT_SECRET_KEY)
    return token


def validate_access_token(token: str, db: db_dependency) -> bool | Student:
    """Function that validates the provided access token."""
    try:
        payload: dict = jwt.decode(jwt=token, key=JWT_SECRET_KEY, algorithms=[JWT_ALGORITHM])
        user_id = payload.get("uid")

        if not user_id:
            return False

        user = db.get(Student, user_id)

        if not user:
            return False

        return user

    except InvalidTokenError:
        return False
