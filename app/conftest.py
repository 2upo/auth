import pytest

@pytest.fixture(scope="session")
def f():
    return object()

