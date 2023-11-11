from hand import Hand
from card import Card
from deck import Deck


def test_card_value():
    assert Card(Card.CLUBS, "2").value() == 2
    assert Card(Card.CLUBS, "4").value() == 4
    assert Card(Card.HEARTS, "10").value() == 10
    assert Card(Card.HEARTS, "K").value() == 10
    assert Card(Card.HEARTS, "Q").value() == 10
    assert Card(Card.HEARTS, "J").value() == 10
    assert Card(Card.HEARTS, "A").value() == 11


def test_card_color():
    assert Card(Card.CLUBS, "2").color() == "black"
    assert Card(Card.SPADES, "2").color() == "black"
    assert Card(Card.HEARTS, "2").color() == "red"
    assert Card(Card.DIAMONDS, "K").color() == "red"


def test_card_repr():
    assert repr(Card(Card.CLUBS, "2")) == "2♣"
    assert repr(Card(Card.SPADES, "10")) == "10♠"
    assert repr(Card(Card.HEARTS, "K")) == "K♥"
    assert repr(Card(Card.DIAMONDS, "A")) == "A♦"


def test_hand_add_one():
    h = Hand()
    h.add(Card(Card.CLUBS, "2"))
    assert h.total() == 2


def test_hand_add_several():
    h = Hand()
    h.add(Card(Card.CLUBS, "2"))
    h.add(Card(Card.CLUBS, "A"))
    assert h.total() == 13
    h.add(Card(Card.CLUBS, "K"))
    assert h.total() == 23


def test_hand_reset():
    h = Hand()
    h.add(Card(Card.CLUBS, "2"))
    h.add(Card(Card.CLUBS, "A"))
    assert h.total() == 13
    h.reset()
    assert h.total() == 0
    h.add(Card(Card.CLUBS, "K"))
    assert h.total() == 10
    h.reset()
    assert h.total() == 0


def test_deck_len():
    d = Deck()
    assert len(d) == 52
    d.deal()
    assert len(d) == 51
    d.deal()
    assert len(d) == 50

    d2 = Deck()
    assert len(d2) == 52
    d2.deal()
    assert len(d2) == 51


def test_deck_is_shuffled():
    d = Deck()
    cards_one = [str(d.deal()) for _ in range(3)]

    d2 = Deck()
    cards_two = [str(d.deal()) for _ in range(3)]

    # shouldn't have drawn the same cards, indicates lack of shuffling
    assert cards_one != cards_two


def test_deck_len_resets():
    d = Deck()
    assert len(d) == 52
    d.deal()
    d.deal()
    assert len(d) == 50
    d.shuffle()
    assert len(d) == 52


def test_deck_reshuffle():
    d = Deck()
    first = d.deal()
    d.shuffle()
    # ensure the card wasn't placed back on top
    assert d.deal() != first
    while len(d) > 1:
        d.deal()
    last = d.deal()
    assert str(first) == str(last)
