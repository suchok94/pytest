import pytest
from src.array import Array


@pytest.mark.parametrize('args, extend_result',
                         [([1, 2, 3, 4, 5], 15),
                          ([-1, -2, -3, -4, -5], -15),
                          ([1, -2, 3, -4, 5], 3),
                          ([0, 0, 0, 0, 0 ], 0),
                          ([1], 1),
                          ([-1], -1)
                          ])
def test_sum_positive(args, extend_result):
    arr = Array(*args)
    assert arr.sum() == extend_result


@pytest.mark.parametrize('args, extend_result',
                         [([1, 2, 3, 4, None], pytest.raises(TypeError)),
                          ([1, 2, 3, 4, 'строка'], pytest.raises(TypeError))
                          ])
def test_sum_negative(args, extend_result):
    arr = Array(*args)
    with extend_result:
        assert arr.sum() == extend_result