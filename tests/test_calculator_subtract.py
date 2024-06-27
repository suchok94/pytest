import pytest
from src.calculator import Calculator


@pytest.mark.parametrize('a, b, extend_result',[
                          (1, 1, 0),
                          (1.5, 1.5, 0),
                          (0, 0, 0),
                          (10, 5, 5),
                          (-3, -26, 23),
                          (0, 2, -2),
                          (5, 0, 5),
                          (0, -8, 8),
                          (-7, 0, -7)
                          ])
def test_subtract_positive(a, b, extend_result):
    calc = Calculator()
    assert calc.subtract(a, b) == extend_result


@pytest.mark.parametrize('a, b, extend_result',
                         [(None, None, pytest.raises(TypeError)),
                          ('', '', pytest.raises(TypeError)),
                          (1, None, pytest.raises(TypeError)),
                          (None, 1, pytest.raises(TypeError)),
                          (1, '', pytest.raises(TypeError)),
                          ('', 1, pytest.raises(TypeError))
                          ])
def test_subtract_negative(a, b, extend_result):
    calc = Calculator()
    with extend_result:
        assert calc.subtract(a, b) == extend_result