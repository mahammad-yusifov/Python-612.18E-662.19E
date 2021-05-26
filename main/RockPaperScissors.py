""" Rock Paper Scissors
----------------------------------------
"""
import random
import os
import re

from pip._vendor.distlib.compat import raw_input

os.system('cls' if os.name == 'nt' else 'clear')
while True:
    print("\n")
    print("Rock, Paper, Scissors - Shoot!")
    userChoice = raw_input("Choose your weapon [R]ock, [P]aper, or [S]cissors: ")
    if not re.match("[SsRrPp]", userChoice):
        print("Please choose a letter:")
        print("[R]ock, [S]cissors or [P]aper.")
        continue

    print("You chose: " + userChoice)
    choices = ['R', 'P', 'S']
    programChoice = random.choice(choices)
    print("I chose: " + programChoice)
    if programChoice == str.upper(userChoice):
        print("Tie! ")
    # if opponentChoice == str("R") and str.upper(userChoice) == "P"
    elif programChoice == 'R' and userChoice.upper() == 'S':
        print("Rock beats scissors, I win! ")
        continue
    elif programChoice == 'S' and userChoice.upper() == 'P':
        print("Scissors beats paper! I win! ")
        continue
    elif programChoice == 'P' and userChoice.upper() == 'R':
        print("Paper beat rock, I win! ")
        continue
    else:
        print("You win!")
