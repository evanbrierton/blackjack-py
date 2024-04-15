from typing import Self

from random import Random
from card import Card
from suit import Suit
from rank import Rank

class Deck:
    def __init__(self):
        self.cards = [Card(suit, rank) for suit in Suit for rank in Rank]
      
    def __str__(self):
        return "\n".join([str(card) for card in self.cards])

    def shuffle(self) -> Self:
        Random().shuffle(self.cards)
        return self

    def draw(self) -> Card:
        return self.cards.pop()
