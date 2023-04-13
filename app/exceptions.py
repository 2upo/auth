from fastapi.exceptions import HTTPException


class BaseServiceException(HTTPException):
    pass