'''
ROSHAMBO PROGRAM
----------------

Create a program that randomly prints 1, 2, or 3.
Expand the program so it randomly prints rock, paper, or scissors using if statements. Don't select from a list.
Add to the program so it first asks the user their choice as well as if they want to quit.
(It will be easier if you have them enter 1 for rock, 2 for paper, and 3 for scissors.)
Add conditional statements to figure out who wins and keep the records
When the user quits print a win/loss record

'''

import random

user = 0
end = False
user_count = 0
total_count = 0

def user_win():     #defining fuction for when the player wins
    print('The player wins!')
    global user_count
    user_count += 1

print('This is a game of rock, paper, scissors.  Enter 1 for rock, 2 for paper, or 3 for scissors.\nTo end the game, enter 0.')
while end == False:
    user = int(input('Please Enter: '))
    comp = random.randint(1, 3)

    if comp == 1:          #assigns comp's number to the corresponding choice
        comp_str = 'Rock'
    elif comp == 2:
        comp_str = 'Paper'
    elif comp == 3:
        comp_str = 'Scissors'

    if user == 1:          #assigns user's number to the corresponding choice
        user_str = 'Rock'
    elif user == 2:
        user_str = 'Paper'
    elif user == 3:
        user_str = 'Scissors'
    else:               #if the user doesnt make a valid response, the program ends
        end = True
        print('Thank you for playing!')
        continue
    #Tells the user their own choice and the computer's choice
    print('\nThe player has chosen '+user_str+', and the computer has chosen '+comp_str+'.')

    total_count += 1
    if user == comp:    #Does statement comparison to detirmine who wins
        print('Tie!')
    elif user == 2 and comp == 1:
        user_win()
    elif user == 3 and comp == 2:
        user_win()
    elif user == 1 and comp == 3:
        user_win()
    else:       #if it isnt a tie, and the user doesnt win, then the computer must win
        print('The computer wins!')

    print('\nThe player has won '+str(user_count)+' of '+str(total_count)+' games.')