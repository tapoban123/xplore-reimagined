from fastapi import APIRouter

student_auth_router = APIRouter(
    prefix="students/auth/",
    tags=["Auth"],
)
