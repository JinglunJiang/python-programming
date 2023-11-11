import pytest
from find_twos import find_twos


@pytest.mark.parametrize(
    "str1,str2,result",
    [
        ("1,2,3", "1", []),
        ("1,2,3", "2", [2]),
        ("1,     2,  3", "2", [2]),            # whitespace
        ("2,23,1", "3,2", [2]),
        ("2,23,1", "1,23,4", [23]),
        ("1,2,2,2", " 2 , 2 , 2", [2]), # no duplicates
        ("2,22,222", "2,22,222", [2, 22, 222]),
        ("2,222,22", "2,222,22", [2, 222, 22]),
    ],
)
def test_find_twos(str1, str2, result):
    assert find_twos(str1, str2) == result
