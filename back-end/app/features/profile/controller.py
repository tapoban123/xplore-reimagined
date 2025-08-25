from fastapi import APIRouter, Depends
from typing import Annotated

from .models import FetchStudentDataModel, FetchStudentPsychometricsModel
from ..auth.student.services import validate_token
from ...database.core import db_dependency
from ...entities.entities import Student
from .services import fetch_user_psychometrics, delete_user_account

user_profile_router = APIRouter(
    prefix="/student",
    tags=["User Profile"],
)


@user_profile_router.get("/data", response_model=FetchStudentDataModel)
def fetch_student_details(user: Annotated[Student, Depends(validate_token)]):
    return user


@user_profile_router.get("/psychometrics", response_model=FetchStudentPsychometricsModel)
def fetch_student_psychometrics(user: Annotated[Student, Depends(validate_token)], db: db_dependency):
    return fetch_user_psychometrics(user, db)


@user_profile_router.delete("/delete")
def delete_student(user: Annotated[Student, Depends(validate_token)], db: db_dependency):
    return delete_user_account(user, db)
