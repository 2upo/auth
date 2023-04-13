import pytest
from .exceptions import NotVerified, UserNotFound

from fastapi.exceptions import HTTPException


@pytest.mark.parametrize("exc_type,status_code,message", [
    [NotVerified, 403, "You are not verified"],
    [UserNotFound, 404, "User not found"]
])
def test_not_verified(exc_type, status_code, message, f):
    with pytest.raises(HTTPException) as error:
        raise exc_type
    assert error.value.status_code == status_code
    assert error.value.detail == message
    assert f



