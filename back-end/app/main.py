from fastapi import FastAPI
from .ai_questionnaire.controller import ai_router

app = FastAPI()
app.include_router(ai_router)


@app.get("/")
def home():
    return "Welcome to AI Career Finder App - Xplore"
