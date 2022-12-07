# pylint: disable=invalid-name
import time
import random


class Game(object):
    rules = [['rock', 'scissors'], ['paper', 'rock'], ['scissors', 'paper']]

    def __init__(self):
        while True:
            userChoice = input("Rock, Paper or Scissors? ")
            if any(userChoice in (match := nested_list) for nested_list in self.rules):
                print("good job!")
                self.choice = userChoice
                self.computerChoice = random.choice(self.rules)
                for item in self.rules:
                    currentItem = item[0]
                    if currentItem == self.choice:
                        self.beats = item[1]
                        return
            else:
                print("incorrect choice!, please choose the correct choice")

    def play(self):
        for index in range(3):
            print(f"Results in {3-index}...")
            time.sleep(0.5)

        if self.choice.lower() == self.computerChoice[0].lower():
            print("It's a tie game! Your choice: " + self.choice +
                  " The Computers choice: " + self.computerChoice[0])
        elif self.choice.lower() != self.computerChoice[0].lower() and self.beats.lower() == self.computerChoice[0].lower():
            print(
                f"{self.choice.lower()}, beats : {self.beats.lower()}, you Win!!")
        else:
            print(
                f"Computer chose {self.computerChoice[0].lower()}, which beats : {self.computerChoice[1].lower()}, you Lose!!")

        time.sleep(1.5)
        ask = input("Would you like to play again? y/n : ")
        if ask == 'y':
            return True
        elif ask == 'n':
            return False


continuePlay = True
while continuePlay:
    game = Game()
    continuePlay = game.play()
