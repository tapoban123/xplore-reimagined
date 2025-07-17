from fastapi import HTTPException, status


class BaseAuthException(HTTPException):
    """Base exception for Authentication."""
    pass


class UserAlreadyExistsException(BaseAuthException):
    def __init__(self):
        message = "User already exists in database."
        super().__init__(status_code=status.HTTP_409_CONFLICT, detail=message)


class UserNotFoundException(BaseAuthException):
    def __init__(self):
        message = "No user found."
        super().__init__(status_code=status.HTTP_404_NOT_FOUND, detail=message)


class InvalidUserCredentialsException(BaseAuthException):
    def __init__(self):
        message = "Invalid user credentials."
        super().__init__(status_code=status.HTTP_401_UNAUTHORIZED, detail=message)
