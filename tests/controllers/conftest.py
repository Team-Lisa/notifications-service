import pytest
from api.Repositories.db import DataBase

@pytest.fixture
def init():
    DataBase()
    return 0
