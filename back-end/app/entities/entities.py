from sqlmodel import SQLModel, Field, Relationship
from datetime import datetime


class Student(SQLModel, table=True):
    __tablename__ = "students"

    id: str = Field(primary_key=True, nullable=False)
    name: str = Field(nullable=False)
    email: str = Field(nullable=False, unique=True)
    password: str = Field(nullable=False)
    date_of_birth: datetime = Field(default=None)
    institution: str = Field(default=None)

    psychometrics: list["StudentPsychometrics"] | None = Relationship(
        back_populates="student", cascade_delete=True
    )


class StudentPsychometrics(SQLModel, table=True):
    __tablename__ = "student_psychometrics"

    id: str = Field(primary_key=True, nullable=False)
    Analytical_Thinking: float | None = Field()
    Creativity: float | None = Field()
    Emotional_Intelligence: float | None = Field()
    Leadership: float | None = Field()
    Communication_Skills: float | None = Field()
    Risk_taking: float | None = Field()
    Attention_to_Detail: float | None = Field()
    Problem_solving: float | None = Field()
    Empathy: float | None = Field()
    Teamwork: float | None = Field()
    Independence: float | None = Field()
    Decision_making: float | None = Field()
    STEM_Interest: float | None = Field()
    Humanities_Interest: float | None = Field()
    Business_Interest: float | None = Field()
    Design_or_Arts: float | None = Field()
    Interest: float | None = Field()
    Social_Work_Interest: float | None = Field()
    report_url: str | None = Field()

    student_id: str | None = Field(foreign_key="students.id", ondelete="CASCADE")
    student: Student | None = Relationship(back_populates="psychometrics")
