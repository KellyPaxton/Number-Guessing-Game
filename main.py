import random
from modules.ls import ls

# computer chooses a random number
x = random.choice(ls)  

y = int(input('Guess a number between 1-10: '))

# checks if the number you chose is the same number the computer chose
if x == y:                      
    print('Good Job! The number was ')
    print(x)
else:
    print('Sorry, the number was ')
    print(x)
