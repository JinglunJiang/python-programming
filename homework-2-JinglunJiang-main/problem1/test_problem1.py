import problem1


def test_satisfy_basic1():
    assert problem1.satisfy(lambda x: x > 10, lambda y: y < 100, [2]) == [(2, False)]


def test_satisfy_basic_few():
    assert problem1.satisfy(lambda x: x > 10, lambda y: y < 100, [1, 20, 200]) == [
        (1, False),
        (20, True),
        (200, False),
    ]


def test_satisfy_empty():
    assert problem1.satisfy(lambda x: x > 10, lambda y: y < 100, []) == []


def test_satisfy_indivisible():
    assert problem1.satisfy(lambda x: x % 2 != 0, lambda x: x % 3 != 0, range(10)) == [
        (0, False),
        (1, True),
        (2, False),
        (3, False),
        (4, False),
        (5, True),
        (6, False),
        (7, True),
        (8, False),
        (9, False),
    ]


def test_satisfy_all_basic():
    funcs = [lambda x: x > 10, lambda y: y < 100]
    assert problem1.satisfy_all(funcs, [1, 20, 200]) == [
        (1, [False, True]),
        (20, [True, True]),
        (200, [True, False]),
    ]


def test_satisfy_all_empty_vals():
    funcs = [lambda x: x > 10, lambda y: y < 100]
    assert problem1.satisfy_all(funcs, []) == []


def test_satisfy_all_empty_funcs():
    funcs = []
    assert problem1.satisfy_all(funcs, [1, 2, 3]) == [
        (1, []),
        (2, []),
        (3, []),
    ]


def test_satisfy_all_many_funcs():
    funcs = [lambda x: True, lambda x: False, lambda x: x == 1, lambda x: x != 2]
    assert problem1.satisfy_all(funcs, [1, 2, 3]) == [
        (1, [True, False, True, True]),
        (2, [True, False, False, False]),
        (3, [True, False, False, True]),
    ]
