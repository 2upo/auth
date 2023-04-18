import pytest

@pytest.fixture(scope="session")
def f():
    return object()


@pytest.fixture(scope="session")
def db_fix():
    pass