from pydantic import BaseModel
from datetime import datetime


class FetchStudentDataModel(BaseModel):
    id: str
    name: str
    email: str
    date_of_birth: datetime | None = None
    institution: str | None = None


class FetchStudentPsychometricsModel(BaseModel):
    id: str
    student_id: str | None
    report_url: str | None
    Analytical_Thinking: float | None
    Creativity: float | None
    Emotional_Intelligence: float | None
    Leadership: float | None
    Communication_Skills: float | None
    Risk_taking: float | None
    Attention_to_Detail: float | None
    Problem_solving: float | None
    Empathy: float | None
    Teamwork: float | None
    Independence: float | None
    Decision_making: float | None
    STEM_Interest: float | None
    Humanities_Interest: float | None
    Business_Interest: float | None
    Design_or_Arts: float | None
    Interest: float | None
    Social_Work_Interest: float | None
