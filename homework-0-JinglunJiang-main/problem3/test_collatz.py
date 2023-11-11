import pytest
from collatz import stopping_time, next_value


@pytest.mark.parametrize(
    "n,next_val",
    [
        (2, 1),
        (3, 10),
        (4, 2),
        (27, 82),
    ],
)
def test_next_value(n, next_val):
    assert next_value(n) == next_val


def test_next_value_int():
    assert isinstance(
        next_value(2), int
    ), "Make sure you're using // for floor division"
    assert isinstance(next_value(3), int)


@pytest.mark.parametrize(
    "n,max_iterations,stop",
    [
        (1, 100, 0),
        (2, 100, 1),
        (3, 100, 7),
        (4, 100, 2),
        (27, 100, 100),
        (27, 200, 111),
    ],
)
def test_collatz_stopping(n, max_iterations, stop):
    assert stopping_time(n, max_iterations) == stop
