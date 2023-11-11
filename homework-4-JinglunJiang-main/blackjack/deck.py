import random
from card import Card

class Deck:
    """
    Initialize a new set of 52 cards.
    Shuffle the cards a the beginning.
    Initialize a list to keep track of the already dealt cards.
    """
    def __init__(self):
        suits = [Card.CLUBS, Card.DIAMONDS, Card.HEARTS, Card.SPADES]
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'K', 'Q', 'A']
        self.cards = [Card(suit, value) for suit in suits for value in values]
        random.shuffle(self.cards)
        self.dealt = []

    def __len__(self):
        """
        Returns the number of cards in the deck.
        """
        return len(self.cards)
    
    def deal(self):
        """
        Pop a card from the cards list and add to the dealt card list.
        Returns the dealt card.
        """
        self.dealt_card = self.cards.pop(0)
        self.dealt.append(self.dealt_card)
        return self.dealt_card
    
    def shuffle(self):
        """
        Shuffle the list of dealt card.
        Put them at the end of the cards list.
        Clear the dealt card list so that it can keep track of next dealt cards again.
        """
        random.shuffle(self.dealt)
        self.cards += self.dealt
        self.dealt.clear()