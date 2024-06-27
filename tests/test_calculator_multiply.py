import pytest
from src.calculator import Calculator


@pytest.mark.parametrize('a, b, extend_result',[
                          (1, 1, 1),
                          (1.5, 1.5, 2.25),
                          (0, 0, 0),
                          (10, 5, 50),
                          (-3, -26, 78),
                          (0, 2, 0),
                          (5, 0, 0),
                          (0, -8, 0),
                          (-7, 0, 0)
                          ])
def test_multiply_positive(a, b, extend_result):
    calc = Calculator()
    assert calc.multiply(a, b) == extend_result


@pytest.mark.parametrize('a, b, extend_result',
                         [(None, None, pytest.raises(TypeError)),
                          ('', '', pytest.raises(TypeError)),
                          (1, None, pytest.raises(TypeError)),
                          (None, 1, pytest.raises(TypeError)),
                          (1, '', pytest.raises(AssertionError)),
                          ('', 1, pytest.raises(AssertionError))
                          ])
def test_multiply_negative(a, b, extend_result):
    calc = Calculator()
    with extend_result:
        assert calc.multiply(a, b) == extend_result