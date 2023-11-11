import pytest
import problem4


@pytest.mark.parametrize(
    "op,a,b,result",
    [
        ("+", 1, 2, 3),
        ("+", "1", "2", "12"),
        ("/", 3, 2, 1.5),
        ("*", "!", 4, "!!!!"),
        ("-", 4, 3, 1),
        ("-", set("ABC"), set("B"), set("AC")),
        ("%", 7, 2, 1),
    ],
)
def test_calc(op, a, b, result):
    assert problem4.calc(op, a, b) == result
