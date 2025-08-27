from fastapi import Depends
from sqlmodel import Session, SQLModel, create_engine
from typing import Annotated

from ..utils.constants import NEON_POSTGRES_DB

# DATABASE_URL = "sqlite:///xplore.db"
# connect_args = {"check_same_thread": False}
# engine = create_engine(DATABASE_URL, connect_args=connect_args, echo=True)

NEON_POSTGRES_DB_URL = NEON_POSTGRES_DB.NEON_POSTGRES_DB_URL.value
engine = create_engine(NEON_POSTGRES_DB_URL)


def create_all_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        # session.connection().execute(text("PRAGMA foreign_keys = ON;"))
        yield session


db_dependency = Annotated[Session(engine), Depends(get_session)]
