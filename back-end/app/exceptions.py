from fastapi import HTTPException, status


class BaseAuthException(HTTPException):
    """Base exception for Authentication."""
    pass


class UserAlreadyExistsException(BaseAuthException):
    def __init__(self):
        message = "User already exists in database."
        super().__init__(status_code=status.HTTP_409_CONFLICT, detail=message)
