import problem3

def test_duplicate_simple():
    assert problem3.duplicate([1,2,3], 3) == [(1, 1, 1), (2, 2, 2), (3, 3, 3)]

def test_duplicate_empty_vals():
    assert problem3.duplicate([], 3) == []

def test_duplicate_zero():
    assert problem3.duplicate([1,2,3], 0) == [(), (), ()]

def test_duplicate_one():
    assert problem3.duplicate([1,2,3], 1) == [(1,), (2,), (3,)]
