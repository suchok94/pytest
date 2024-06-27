import pytest
from src.user import User


@pytest.mark.parametrize('name, age, extend_result',
                         [("Ivan", 16, 17),
                          ("qweasd123", 25, 26)])
def test_get_age(name, age, extend_result):
    user = User(name, age)
    assert user.up_age() == extend_result
