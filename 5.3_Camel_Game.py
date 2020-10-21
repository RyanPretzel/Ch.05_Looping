'''
CAMEL GAME
----------
The pseudo-code for how to code this game is in Chapter 5 of the Python Jedi book


Ok so here is the situation
You are an ADC, and there is farm in the bot lane
However, the Mid laner is missing, and he is chasing you and your support.
Try to escape to your fountain with the most CS possible
'''

import random

done = False
cs = 0
distance_fountain = 0
support_tiredness = 0
zed = random.randint(10,15)

while done == False:
    print('\nA) Drink from your canteen\nB) Moderate Speed\nC) Full Speed\nD) Rest\nE) Status Check\nG) Greed for the CS\nQ) Quit')
    choice = input('\nPlease choose your action: ')
    if choice.upper() == 'Q': #End game if user wants to
        done = True
        continue
    else:
        print('Zed has caught up')
    print(str(zed))





