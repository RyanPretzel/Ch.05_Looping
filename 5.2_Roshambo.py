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

print('This is a game of rock, paper, scissors.  Enter 1 for rock, 2 for paper, or 3 for scissors.')
while end == False:
    user = input('Please Enter: ')
    comp = random.randint(1, 3)
    print('User is '+str(user))  #Printing for debug
    print('Comp is '+str(comp))
    if int(user) == comp:      #if both players choose the same comp, it ties
        print('Tie!')
    elif int(user) == 1 and comp == 3:
        print('rock')
    elif int(user) == 2:
        print('paper')
    elif int(user) == 3:
        print('scissors')
    else:
        end = True