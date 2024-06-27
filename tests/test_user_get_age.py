import pytest
from src.user import User


@pytest.mark.parametrize('name, age, extend_result',
                         [("Ivan", 16, 16),
                          ("qweasd123", 25, 25)])
def test_get_age(name, age, extend_result):
    user = User(name, age)
    assert user.get_age() == extend_result
