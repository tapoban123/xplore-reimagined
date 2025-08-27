from pydantic import BaseModel


class QuestionsModel(BaseModel):
    question: str
    answer: str


class QuestionsWithAnswersRequestModel(BaseModel):
    questions_with_answers: list[QuestionsModel]
