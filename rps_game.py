# pylint: disable=invalid-name
import time
import random
from dataclasses import dataclass


@dataclass
class Game(object):
    rules = [['rock', 'scissors'], ['paper', 'rock'], ['scissors', 'paper']]

    def __init__(self) -> None:
        while True:
            userChoice = input("Rock, Paper or Scissors? ")
            if any(userChoice in (match := nested_list) for nested_list in self.rules):
                print("good job!")
                self.choice = userChoice.upper()
                self.computerChoice = random.choice(self.rules)
                self.beats = match[1].upper()
                break
            else:
                print("incorrect choice!, please choose the correct choice")

    def play(self) -> bool:
        for index in range(3):
            print(f"Results in {3-index}...")
            time.sleep(0.5)

        if self.choice == self.computerChoice[0].upper():
            print(f"It's a tie game! Your choice: {self.choice} " +
                  f"The Computers choice: {self.computerChoice[0].upper()}")
        elif self.choice != self.computerChoice[0].upper() \
                and self.beats == self.computerChoice[0].upper():
            print(f"{self.choice}, beats : {self.beats}, you Win!!")
        else:
            print(f"Computer chose {self.computerChoice[0].upper()}, " +
                  f"which beats : {self.computerChoice[1].upper()}, you Lose!!")

        time.sleep(1)
        ask = input("Would you like to play again? y/n : ")
        if ask == 'y':
            return True
        elif ask == 'n':
            return False


continuePlay = True
while continuePlay:
    game = Game()
    continuePlay = game.play()
