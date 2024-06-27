import pytest
from src.user import User


@pytest.mark.parametrize('name, age, extend_result',
                         [("Ivan", 16, User('Ivan', 16))])
def test_init_possitive(name, age, extend_result):
    user = User(name, age)
    assert user.name == extend_result.name and user.age == extend_result.age




def test_init_negative():

    user = User('Ivan', 'шестнадцать')
    assert isinstance(user.name, str)  and isinstance(user.age, int)
