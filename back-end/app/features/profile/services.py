from ...database.core import db_dependency
from ...entities.entities import Student, StudentPsychometrics
from sqlmodel import select


# def fetch_user_data(user: Student, db: db_dependency):
#     pass


def fetch_user_psychometrics(user: Student, db: db_dependency):
    """Fetch values of all psychometric parameters of the user."""
    query = select(StudentPsychometrics).where(StudentPsychometrics.student_id == user.id)
    result = db.exec(query).one()
    return result


def delete_user_account(user: Student, db: db_dependency):
    """Delete the account of the student."""
    query = select(Student).where(Student.id == user.id)
    result =  db.exec(query).one()

    db.delete(result)
    db.commit()
    return {"details": "success"}
