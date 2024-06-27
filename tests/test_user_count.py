import pytest
from src.user import User


@pytest.mark.parametrize('name, age, extend_result',
                         [("Ivan", 16, 1)])
def test_count(name, age, extend_result):
    user = User(name, age)
    assert user.count == extend_result
