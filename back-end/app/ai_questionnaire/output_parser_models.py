from pydantic import BaseModel, Field


class QuestionModel(BaseModel):
    question: str = Field(description="The psychometric question for the user.")
    choices: list[str] = Field(
        description="List containing four choices for the question."
    )


class AllQuestionsModel(BaseModel):
    all_questions: list[QuestionModel] = Field(
        description="List containing all the psychometric questions for the user."
    )


class CareerModel(BaseModel):
    career: str = Field(description="Name of the career")
    explanation: str = Field(
        description="Explanation of why the career is suitable for the student."
    )


class PsychometricsModel(BaseModel):
    parameter: str = Field(description="Name of the parameter")
    score: float = Field(
        description="Score of the parameter from 0 to 10 based on the user's answers"
    )


class CareersOutputModel(BaseModel):
    careers: list[CareerModel] = Field(
        description="Careers for the user.", max_length=3, min_length=3
    )
    psychometrics: list[PsychometricsModel] = Field(
        description="Psychometric parameters with a score from 0 to 10."
    )
