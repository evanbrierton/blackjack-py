from game import Game
from action import Action
from outcome import Outcome

game = Game()

while not game.over:
    print(f"{game.player}\n")

    action = input("Hit or stand? ").lower()

    match action:
        case Action.HIT.value:
            game.hit()
        case Action.STAND.value:
            game.stand()

print(f"\nHand: {game.player} ({game.player_score()})")

if game.stood:
    print(f"Dealer: {game.dealer} ({game.dealer_score()})")

print()

match game.outcome():
    case Outcome.WIN:
        print("You win!")
    case Outcome.LOSS:
        print("You lose!")
    case Outcome.TIE:
        print("It's a tie!")
