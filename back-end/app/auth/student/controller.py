from fastapi import APIRouter

from app.database.core import db_dependency
from .services import create_new_student
from .models import SignUpUserModel, LoginInUserModel

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
