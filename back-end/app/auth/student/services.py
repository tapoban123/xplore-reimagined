from sqlmodel import Field, Session, SQLModel, create_engine, select


DATABASE_URL = "sqlite:///xplore.db"

connect_args = {"check_same_thread": False}
engine = create_engine(DATABASE_URL, connect_args=connect_args)
