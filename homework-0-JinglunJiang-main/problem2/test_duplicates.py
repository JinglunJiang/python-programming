from duplicates import find_duplicates


def test_no_duplicates():
    assert find_duplicates([1, 2, 3]) == []


def test_simple_duplicates():
    assert find_duplicates([1, 2, 1, 2, 3]) == [1, 2]


def test_many_duplicates():
    assert find_duplicates([1] * 10) == [1]


def test_duplicates_in_string():
    assert find_duplicates("apple") == ["p"]
