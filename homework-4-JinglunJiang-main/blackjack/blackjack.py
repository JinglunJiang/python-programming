from rich.prompt import Confirm
from card import Card
from deck import Deck
from hand import Hand
from utils import draw_card_table, does_player_hit


def main():
    """
    Game Implementation.
    """
    # TODO: initialize game

    deck = Deck() # Initialize a shuffled deck
    num_dealer_wins = 0 # Count from each time the game begins
    num_player_wins = 0

    while True:
        # TODO: play round of Blackjack as described in README
        deck.shuffle() 
        # After every round, the dealt cards are shuffled and put at the bottom
        dealer = Hand()
        player = Hand()
        #Initialize the dealer's hand and player's hand after each round

        dealer.add(deck.deal())
        dealer.add(deck.deal())
        player.add(deck.deal())
        player.add(deck.deal())
        #Assign two cards for each player each round

        while True:
            # The player's turn
            draw_card_table(deck, dealer, player, num_dealer_wins, num_player_wins)
            if player.total() > 21:
                break
            if does_player_hit():
                player.add(deck.deal())
            else:
                break
        
        while dealer.total() < 17:
            # The dealer's turn
            dealer.add(deck.deal())

        # Calculate who wins after each round
        if player.total() > 21:
            num_dealer_wins += 1
        elif dealer.total() > 21:
            num_player_wins += 1
        elif player.total() > dealer.total():
            num_player_wins += 1
        elif player.total() < dealer.total():
            num_dealer_wins += 1

        draw_card_table(deck, dealer, player, num_dealer_wins, num_player_wins)
        # Show the results again after each round
        # end of round

        if not Confirm.ask("Play again?"):
            break

if __name__ == "__main__":
    main()
