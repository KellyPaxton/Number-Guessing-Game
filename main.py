#!/usr/bin/env python3

import random
from modules.ls import ls

# computer chooses a random number
x = random.choice(ls) 

# checks if the number you chose is the same number the computer chose
while True:
    y = int(input('Guess a number between 1-10: '))
    if y != x:
        print("Sorry, Try Again!")
    else:
        print("Great Job! The number Was ", x)
        break
