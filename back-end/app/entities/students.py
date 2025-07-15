from sqlmodel import SQLModel, Field


class Student(SQLModel, table=True):
    id: str = Field(primary_key=True, nullable=False)
    name: str = Field(nullable=False)
    email: str = Field(nullable=False, unique=True)
    password: str = Field(nullable=False)
