from fastapi import APIRouter, Depends
import cloudinary.uploader

from .services import (
    get_questions,
    get_careers,
    generate_pdf,
    store_psychometrics_to_db,
)
from .models import QuestionsWithAnswersRequestModel
from ..auth.student.services import validate_token
from ...database.core import db_dependency
from typing import Annotated
from ...entities.entities import Student

ai_router = APIRouter(
    prefix="/ai",
    tags=["AI Questionnaire"],
)


@ai_router.get("/questions")
def get_psychometric_questionnaire():
    return get_questions()


@ai_router.post("/careers")
def get_careers_for_user(
    user: Annotated[Student, Depends(validate_token)],
    qna: QuestionsWithAnswersRequestModel,
    db: db_dependency,
):
    careers_output = get_careers(qna.questions_with_answers)
    pdf = generate_pdf(user, careers_output)

    result = cloudinary.uploader.upload(
        file=pdf,
        asset_folder="reports",
        public_id=f"report_{user.id}",
        overwrite=True,
        resource_type="raw",
    )

    report_url = result["secure_url"]

    store_psychometrics_to_db(
        db=db,
        careers_output=careers_output,
        report_url=report_url,
        student_id=user.id,
    )

    final_output = {"report": report_url, **careers_output.model_dump()}

    return final_output
