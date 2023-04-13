from ..exceptions import BaseServiceException
import http


class NotVerified(BaseServiceException):
    def __init__(self):
        super().__init__(
            status_code=http.HTTPStatus.FORBIDDEN,
            detail="You are not verified"
        )

class UserNotFound(BaseServiceException):
    def __init__(self):
        super().__init__(
            status_code=http.HTTPStatus.NOT_FOUND,
            detail="User not found"
        )