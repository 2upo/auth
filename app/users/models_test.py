import pytest
from .models import User
import uuid


def test_user_model():
    user = User(
        id = uuid.uuid4(),
        name = 'aboba',
        email = 'some@gmail.com',
        password = '1234',
        verified = True,
    )

    assert user
    assert user.to_dict()

