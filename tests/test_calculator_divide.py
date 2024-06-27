import pytest
from src.calculator import Calculator


@pytest.mark.parametrize('a, b, extend_result',
                         [(1, 1, 1),
                          (1.5, 1.5, 1),
                          (10, 5, 2),
                          (-3, -26, 0.11538461538461539),
                          (0, 2, 0),
                          (0, -8, 0)
                          ])
def test_divide_positive(a, b, extend_result):
    calc = Calculator()
    assert calc.divide(a, b) == extend_result


@pytest.mark.parametrize('a, b, extend_result',
                         [(None, None, pytest.raises(TypeError)),
                          ('', '', pytest.raises(TypeError)),
                          (1, None, pytest.raises(TypeError)),
                          (None, 1, pytest.raises(TypeError)),
                          (1, '', pytest.raises(TypeError)),
                          ('', 1, pytest.raises(TypeError)),
                          (0, 0, pytest.raises(ZeroDivisionError)),
                          (5, 0, pytest.raises(ZeroDivisionError)),
                          (-7, 0, pytest.raises(ZeroDivisionError))
                          ])
def test_divide_negative(a, b, extend_result):
    calc = Calculator()
    with extend_result:
        assert calc.divide(a, b) == extend_result