class Hand:
    """
    Initialize the cards, and the sum for the new instance = 0.
    """
    def __init__(self):
        self.cards = []
        self.sum = 0
        
    def reset(self):
        """
        Remove all the cards from the current instance.
        Initialize the current sum.
        """
        self.cards.clear()
        self.sum = 0
    
    def add(self, card):
        """
        Add card to the cards list.
        Recalculate the current sum by adding the added card's value.
        """
        self.cards.append(card)
        self.sum += card.value()

    def total(self):
        """
        Return the current sum of the instance.
        """
        return self.sum