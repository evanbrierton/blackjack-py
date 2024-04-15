from typing import Self

from outcome import Outcome
from deck import Deck
from card import Card
from rank import Rank

class Game:
    def __init__(self):
        self.stood = False
        self.over = False
        self.deck = Deck()
        self.deck.shuffle()
        self.player: set['Card'] = set()
        self.dealer: set['Card'] = set()
        self.start()

    def start(self) -> Self:
        self.hit()
        self.dealer.add(self.deck.draw())
        self.hit()

        return self

    def hit(self) -> Self:
        self.player.add(self.deck.draw())

        if self.player_score() > 21:
            self.over = True

        return self

    def stand(self) -> Self:
        self.stood = True

        while self.dealer_score() < 17:
            self.dealer.add(self.deck.draw())
          
        self.over = True

        return self
        
    def outcome(self) -> Outcome:
        player_score = self.player_score()
        dealer_score = self.dealer_score()

        if player_score > 21:
            return Outcome.LOSS
        
        if dealer_score > 21:
            return Outcome.WIN
        
        if player_score == dealer_score:
            return Outcome.TIE
        
        return Outcome.WIN if player_score > dealer_score else Outcome.LOSS
    
  
    def player_score(self) -> int:
        score = Game.score(self.player)
        aces = sum([1 for card in self.player if card.rank == Rank.ACE])

        while score > 21 and aces > 0:
            score -= 10
            aces -= 1

        return score
    
    def dealer_score(self) -> int:
        return Game.score(self.dealer)

    @staticmethod
    def value(card: Card) -> int:
        return 11 if card.rank == Rank.ACE else min(card.rank.value, 10)
    
    @staticmethod
    def score(hand: set['Card']) -> int:
        return sum([Game.value(card) for card in hand])
    