from grid import get_sector

grid3x3 = [
    ["A", "B", "C"],
    ["D", "E", "F"],
    ["G", "H", "I"],
]

def test_get_sector1():
    assert get_sector(grid3x3, (0, 1), (0, 2)) == ["A", "B"]


def test_get_sector2():
    assert get_sector(grid3x3, (0, 2), (0, 1)) == ["A", "D"]


def test_get_sector3():
    assert get_sector(grid3x3, (0, 3), (0, 3)) == ["A", "B", "C", "D", "E", "F", "G", "H", "I"]


def test_get_sector4():
    assert get_sector(grid3x3, (1, 3), (1, 3)) == ["E", "F", "H", "I"]


def test_get_sector5():
    assert get_sector(grid3x3, (1, 2), (1, 2)) == ["E"]


def test_get_sector6():
    assert get_sector(grid3x3, (0, 2), (0, 2)) == ["A", "B", "D", "E"]
