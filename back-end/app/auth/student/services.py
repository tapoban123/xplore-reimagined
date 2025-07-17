import uuid

from passlib.context import CryptContext
import jwt
from jwt.exceptions import InvalidTokenError
from datetime import datetime, timedelta, timezone
from sqlmodel import select

from app.utils.env_secrets import JWT_SECRETS
from app.database.core import db_dependency
from app.entities.students import Student
from app.exceptions import UserAlreadyExistsException, UserNotFoundException, InvalidUserCredentialsException

JWT_SECRET_KEY = JWT_SECRETS.JWT_SECRET_KEY.value
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


def create_access_token(uid: str):
    """Function that generates a new access token from the user id. Token expires after 30 days."""
    payload: dict[str, datetime | str] = {"uid": uid}
    exp_claim = {"exp": datetime.now(tz=timezone.utc) + timedelta(days=30)}
    payload.update(exp_claim)
    token = jwt.encode(payload=payload, algorithm=JWT_ALGORITHM, key=JWT_SECRET_KEY)
    return token


def validate_access_token(token: str):
    """Function that validates the provided access token."""
    pass
