import pytest
from src.array import Array


@pytest.mark.parametrize('args, extend_result',
                         [([1, 2, 3, 4, 5], 3),
                          ([-1, -2, -3, -4, -5], -3),
                          ([1, -2, 3, -4, 5], 0.6),
                          ([0, 0, 0, 0, 0 ], 0),
                          ([1], 1),
                          ([-1], -1)
                          ])
def test_average_positive(args, extend_result):
    arr = Array(*args)
    assert arr.average() == extend_result


@pytest.mark.parametrize('args, extend_result',
                         [([1, 2, 3, 4, None], pytest.raises(TypeError)),
                          ([1, 2, 3, 4, 'строка'], pytest.raises(TypeError))
                          ])
def test_average_negative(args, extend_result):
    arr = Array(*args)
    with extend_result:
        assert arr.average() == extend_result