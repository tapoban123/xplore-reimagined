from pydantic import BaseModel, Field


class QuestionModel(BaseModel):
    question: str = Field(description="The psychometric question for the user.")
    choices: list[str] = Field(description="List containing four choices for the question.")


class AllQuestionsModel(BaseModel):
    all_questions: list[QuestionModel] = Field(
        description="List containing all the psychometric questions for the user.")


class CareersOutputModel(BaseModel):
    careers: list[str] = Field(description="Three most suitable career titles for the user.")
