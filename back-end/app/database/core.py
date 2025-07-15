from fastapi import Depends
from sqlmodel import Session, SQLModel, create_engine
from typing import Annotated

DATABASE_URL = "sqlite:///xplore.db"

connect_args = {"check_same_thread": False}
engine = create_engine(DATABASE_URL, connect_args=connect_args)


def create_all_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session


db_dependency = Annotated[Session, Depends(get_session)]
