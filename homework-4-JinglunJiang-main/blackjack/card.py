class Card:
    # Class Attributes: Can be referenced as Card.CLUBS, Card.SUIT_SYMBOLS, etc.
    # DO NOT MODIFY
    """
    Initialize the suit of a card and the value of a card.
    """
    CLUBS = "clubs"
    DIAMONDS = "diamonds"
    HEARTS = "hearts"
    SPADES = "spades"
    SUIT_SYMBOLS = {
        CLUBS: "♣",
        SPADES: "♠",
        HEARTS: "♥",
        DIAMONDS: "♦",
    }

    # TODO: add your class definition here
    def __init__(self, suit, value):
        self.suit = suit
        self.card_value = value 

    def value(self):
        """
        Evaluate the numerical value of a card based on the string value.
        """
        if self.card_value in ("K", "Q", "J"):
            return 10
        elif self.card_value == "A":
            return 11
        else:
            return int(self.card_value)
    
    def color(self):
        """
        Returns the color of the card based on their suits.
        """
        if self.suit in (Card.HEARTS, Card.DIAMONDS):
            return "red"
        else:
            return "black"
        
    def __repr__(self):
        """
        Shows the card with its value and suit.
        """
        return f"{self.card_value}{Card.SUIT_SYMBOLS[self.suit]}"