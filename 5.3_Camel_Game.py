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
mana_pots = 2
mana = 550
support_unhappiness = 0
zed_dist = random.randint(18, 25)
zed_live = True
support = True

while done == False:
    print('\nA) Drink a mana potion\nB) Moderate Speed away\nC) Full Speed away\nD) Rest\nE) Status Check\nF) Quickly get the CS\nG) Greed for the CS\nH) Share the CS with your support\nQ) Quit')
    choice = input('\nPlease choose your action: ')
    if choice.upper() == 'Q': #End game if user wants to
        done = True
        continue
    elif choice.upper() == 'A':     #if user drinks mana potion
        if mana_pots >= 1:
            print('You drink a mana potion and receive 100 mana')
            mana += 100
            mana_pots -= 1
        else:
            print('You do not have enough mana potions to do that.')
    elif choice.upper() == 'B':     #if user runs at moderate speed
        temp_distance = random.randint(8,13)
        zed_dist += temp_distance - random.randint(10,15)
        support_unhappiness += random.randint(1,2)
        print('You are running away from Zed.  You are now '+str(zed_dist)+' units away from Zed')
    elif choice.upper() == 'C':  # if user runs at high speed
        temp_distance = random.randint(16, 20)
        zed_dist += temp_distance - random.randint(10, 15)
        support_unhappiness += random.randint(1, 3)
        print('You are quickly running away from Zed.  You are now '+str(zed_dist)+' units away from Zed')
    elif choice.upper() == 'D':
        support_unhappiness = 0
        zed_dist -= random.randint(10,15)
        print('Your support is now happy.')
    elif choice.upper() == 'E':     #if user does a status check, prints out status of all variables
        print('\nMana:', mana,'\nMana Potions:', mana_pots,'\nSupport Unhappiness:', support_unhappiness, '\nDistance from Zed:', zed_dist, '\nCS:' ,cs)
    elif choice.upper() == 'F':     #user quickly gets the wave
        temp_mana = random.randrange(130, 161, 15)
        mana -= temp_mana
        print('\nYou quickly clear the wave, but you use '+str(temp_mana)+' mana.  You now have '+str(mana)+' mana.')
        cs += random.randint(5,7)
        zed_dist -= random.randint(10,15)
    elif choice.upper() == 'G':     #slowly greed for the wave
        cs += random.randint(5,7)
        zed_dist -= random.randint(14,18)
        print('You now have '+str(cs)+' cs.')
    elif choice.upper() == 'H':     #share the wave with the support.
        cs += random.randint (2,3)
        support_unhappiness = 0
        zed_dist -= 8,12
        print('You')

    #ways to die
    if zed_dist <= 0:
        print('Zed has jumped onto you.  You have died.')
        done = True
        continue
    elif zed_dist <= 14:
        print('Zed is too close for comfort.')

    if support == True:     #If the support is still there
        if support_unhappiness >= 20:       #if he is too unhappy he is just gone
            support = False
            print('You support has left you')
        elif support_unhappiness >= 13:     #if he is kinda unhappy he might leave
            if random.randint(1,3) == 3:
                support = False
                print('Your support has left you')
            else:                           #warning that he might leave
                print('Your support is unhappy')
        elif support_unhappiness >8:
            print('Your support is unhappy')



