# pylint: disable=invalid-name
from time import sleep
import random
from dataclasses import dataclass
import sys


@dataclass
class Game(object):
    choices = {
        "ROCK": ("SCISSORS", "You win!"),
        "PAPER": ("ROCK", "You lose!"),
        "SCISSORS": ("PAPER", "You win!"),
    }

    def __init__(self) -> None:        
        while True:
            self.choice = input(
                "Rock, Paper or Scissors? or type ""exit"" to leave the game").upper()
            if self.choice == "EXIT":
                sys.exit()
            elif self.choice not in self.choices:
                print("Invalid choice. Please try again.")
            else:
                self.computerChoice = random.choice(list(self.choices.items()))
                break

    def play(self) -> bool:
        for countdown in range(3, 0, -1):
            print(f"Results in {countdown}...")
            sleep(0.5)

        outcome = self.choices.get(self.choice, self.computerChoice[0])

        if self.choice == self.computerChoice[0]:
            print(f"It's a tie game! Your choice: {self.choice} " +
                  f"The Computers choice: {self.computerChoice[0]}")
        else:
            print(f"The Computers choice: {self.computerChoice[0]} " +
                  f"Your choice: {self.choice}: {outcome[1]}")

        sleep(1)
        ask = input('Would you like to play again? y/n (or anything else) : ')
        return True if ask == 'y' else False


if __name__ == '__main__':
    for continue_play in iter(lambda: Game().play(), False):
        pass
