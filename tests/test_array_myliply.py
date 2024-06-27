import pytest
from src.array import Array


@pytest.mark.parametrize('args, extend_result',
                         [([1, 2, 3, 4, 5], 120),
                          ([-1, -2, -3, -4, -5], -120),
                          ([1, -2, 3, -4, 5], 120),
                          ([0, 0, 0, 0, 0 ], 0),
                          ([1], 1),
                          ([-1], -1)
                          ])
def test_multiply_positive(args, extend_result):
    arr = Array(*args)
    assert arr.multiply() == extend_result


@pytest.mark.parametrize('args, extend_result',
                         [([1, 2, 3, 4, None], pytest.raises(TypeError)),
                          ([1, 2, 3, 4, 'строка'], pytest.raises(AssertionError))
                          ])
def test_multiply_negative(args, extend_result):
    arr = Array(*args)
    with extend_result:
        assert arr.multiply() == extend_result