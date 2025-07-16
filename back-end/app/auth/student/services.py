import uuid

from passlib.context import CryptContext
import jwt
from jwt.exceptions import InvalidTokenError
from datetime import datetime, timedelta, timezone
from sqlmodel import select

from app.utils.env_secrets import JWT_SECRETS
from app.database.core import db_dependency
from app.entities.students import Student
from app.exceptions import UserAlreadyExistsException

JWT_SECRET_KEY = JWT_SECRETS.JWT_SECRET_KEY.value
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_DAYS = 30

bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def user_exists(email: str, db: db_dependency) -> bool:
    query = select(Student).where(Student.email == email)
    user = len(list(db.exec(query))) > 0
    return user


def create_new_student(name: str, email: str, password: str, db: db_dependency):
    """Function to sign up new students to our platform."""
    if user_exists(email, db):
        raise UserAlreadyExistsException()

    new_user = Student(
        id=uuid.uuid4().hex,
        name=name,
        email=email,
        password=bcrypt_context.hash(password)
    )
    db.add(new_user)
    db.commit()

    return {"details": "success"}


def login_existing_student(email: str, password: str, db: db_dependency):
    """Function that logs in existing student."""
    pass


def create_access_token(id: str):
    """Function that generates a new access token from the user id. Token expires after 30 days."""
    pass


def validate_access_token(token: str):
    """Function that validates the provided access token."""
    pass
