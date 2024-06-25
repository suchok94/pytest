import pytest
from src.calculator import Calculator

@pytest.mark.parametrize('a, b, extend_result',[
                          (1, 1, 2),
                          (1.5, 1.5, 3.0),
                          (0, 0, 0),
                          (10, 5, 15),
                          (-3, -26, -29),
                          (0, 2, 2),
                          (5, 0, 5),
                          (0, -8, -8),
                          (-7, 0, -7)
                          ])
def test_add_positive(a, b, extend_result):
    calc = Calculator()
    calc.add(a, b) == extend_result


@pytest.mark.parametrize('a, b, extend_result',
                         [(None, None, pytest.raises(TypeError)),
                          ('', '', pytest.raises(AssertionError))
                          ])
def test_add_negative(a, b, extend_result):
    calc = Calculator()
    with extend_result:
        assert calc.add(a, b) == extend_result
    # try:
    #     calc.add(a, b) == extend_result
    #     assert False
    # except:
    #     assert 'Куда пишется эта хрень???'
