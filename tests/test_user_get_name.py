import pytest
from src.user import User


@pytest.mark.parametrize('name, age, extend_result',
                         [("Ivan", 16, 'Ivan'),
                          ("qweasd123", 16, 'qweasd123')])
def test_get_name(name, age, extend_result):
    user = User(name, age)
    assert user.get_name() == extend_result
