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
    assert calc.add(a, b) == extend_result


@pytest.mark.parametrize('a, b, extend_result',
                         [(None, None, pytest.raises(TypeError)),
                          ('', '', pytest.raises(AssertionError)),
                          (1, None, pytest.raises(TypeError)),
                          (None, 1, pytest.raises(TypeError)),
                          (1, '', pytest.raises(TypeError)),
                          ('', 1, pytest.raises(TypeError))
                          ])
def test_add_negative(a, b, extend_result):
    calc = Calculator()
    with extend_result:
        assert calc.add(a, b) == extend_result
