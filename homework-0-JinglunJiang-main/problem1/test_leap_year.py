import pytest
from leap_year import is_leap_year


@pytest.mark.parametrize(
    "year,output",
    [
        (2020, True),
        (2021, False),
        (2022, False),
        (1900, False),
        (2000, True),
        (-4, False),
        (-1, False),
    ],
)
def test_leap_year(year, output):
    assert is_leap_year(year) == output
