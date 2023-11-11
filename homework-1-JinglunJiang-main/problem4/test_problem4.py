from io import StringIO
import pathlib
from problem4 import fill_completions, find_completions


def test_fill_completions_basic():
    completions = fill_completions(StringIO("ace ape"))
    assert completions == {
        (0, "a"): {"ace", "ape"},
        (1, "c"): {"ace"},
        (1, "p"): {"ape"},
        (2, "e"): {"ace", "ape"},
    }


def test_fill_completions_lowercase():
    completions = fill_completions(StringIO("aCE APE"))
    assert completions == {
        (0, "a"): {"ace", "ape"},
        (1, "c"): {"ace"},
        (1, "p"): {"ape"},
        (2, "e"): {"ace", "ape"},
    }


def test_fill_completions_strip_chars():
    completions = fill_completions(StringIO("'ace, ape.'"))
    assert completions == {
        (0, "a"): {"ace", "ape"},
        (1, "c"): {"ace"},
        (1, "p"): {"ape"},
        (2, "e"): {"ace", "ape"},
    }


def test_fill_completions_ignore_non_alpha_words():
    completions = fill_completions(StringIO("try7 ain't"))
    assert completions == {}


def test_fill_completions_ignore_short_alpha_words():
    completions = fill_completions(StringIO("a I"))
    assert completions == {}


def test_fill_completions_all_articles():
    fd = open(pathlib.Path(__file__).parent / "articles.txt")
    completions = fill_completions(fd)
    # update these if articles.txt changes
    assert len(completions[0, 'a']) == 355
    assert len(completions[4, 's']) == 323
    assert len(completions) == 340

cdict1 = {
    (0, "a"): {"ace", "ape"},
    (1, "c"): {"ace"},
    (1, "p"): {"ape"},
    (2, "e"): {"ace", "ape"},
}

def test_find_completions_basic():
    assert find_completions("a", cdict1) == {"ace", "ape"}
    assert find_completions("ac", cdict1) == {"ace"}
    assert find_completions("ace", cdict1) == {"ace"}


def test_find_completions_empty():
    assert find_completions("z", cdict1) == set()
    assert find_completions("zc", cdict1) == set()
    assert find_completions("ax", cdict1) == set()
    assert find_completions("aci", cdict1) == set()
    assert find_completions("aces", cdict1) == set()
