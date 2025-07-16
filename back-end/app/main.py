from fastapi import FastAPI
from .ai_questionnaire.controller import ai_router
from contextlib import asynccontextmanager
from .database.core import create_all_tables, db_dependency
from .auth.student.controller import student_auth_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Code to execute when before api starts accepting requests
    print("Running start event")
    create_all_tables()

    yield
    # Code to execute when after exiting app


app = FastAPI(lifespan=lifespan)
app.include_router(ai_router)
app.include_router(student_auth_router)


@app.get("/")
def home():
    return "Welcome to AI Career Finder App - Xplore"
