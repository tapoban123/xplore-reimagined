from fastapi import APIRouter
from .services import get_questions, get_careers
from .models import QuestionsWithAnswersRequestModel

ai_router = APIRouter(
    prefix="/ai",
    tags=["AI Questionnaire"],
)


@ai_router.get("/questions")
def get_psychometric_questionnaire():
    return get_questions()


@ai_router.post("/careers")
def get_careers_for_user(qna: QuestionsWithAnswersRequestModel):
    return get_careers(qna)
