import problem5

def test_list_range_basic():
    assert problem5.list_range((1, 3), [[1, 3, 2], [9, 87, 1], [2, 1]]) == [[1, 3, 2], [2, 1]]


def test_list_range_empty():
    assert problem5.list_range((1, 3), []) == []


def test_list_inner_empty():
    assert problem5.list_range((1, 3), [[]]) == [[]]


def test_list_range_no_matches():
    assert problem5.list_range((1, 3), [[99], [1, 2, 3, 99], [-5, 1, 2]]) == []


def test_list_range_all():
    assert problem5.list_range((1, 300), [[1, 3, 2], [9, 87, 1], [2, 1]]) == [[1, 3, 2], [9, 87, 1], [2, 1]]
