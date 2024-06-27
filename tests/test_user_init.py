import pytest
from src.user import User


@pytest.mark.parametrize('name, age, extend_result',
                         [("Ivan", 16, User('Ivan', 16))])
def test_init_possitive(name, age, extend_result):
    user = User(name, age)
    assert user.name == extend_result.name and user.age == extend_result.age



@pytest.mark.parametrize('name, age',
                         [("Ivan", 'шестнадцать'),
                          ('Ivan', 666),
                          ('Ivan', -20)
                          ])
def test_init_negative(name, age):
    user = User(name, age)
    assert isinstance(user.name, str)  and isinstance(user.age, int) and user.age in range(1, 100)
