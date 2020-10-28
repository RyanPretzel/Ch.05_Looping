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
support = False
tower = False
turn = 0
flash = True

def zed_turn():
    global turn
    global done

    print('\nYou try to turn and kill Zed')
    if support == False:  # # If there is no support, then it will subtract 50 from final calculation
        calc_support = 50
    else:
        calc_support = 0
    if tower == True:  # # If under tower, plus 30
        calc_tower = 30
    else:
        calc_tower = 0
    if mana <= 150:  # # if less than 150 mana, then subtract 25
        calc_mana = 25
    else:
        calc_mana = 0
    turn = (random.randint(cs - 10, cs + 25) - calc_support + calc_tower - calc_mana) / 100

    if turn >= 1:  # # if the turn is sucessful, then kill zed and win the game
        print('You sucessfully kill Zed! Congratulations!')
    if turn < 1:
        print('You were not strong enough, so Zed killed you.  Try getting more CS next time.')
    done = True


while done == False:
    if support == True:
        print('\nA) Drink a mana potion\nB) Moderate Speed away\nC) Full Speed away\nD) Rest\nE) Status Check\nF) Quickly get the CS\nG) Greed for the CS\nH) Share the CS with your support\nI) Turn on Zed\nQ) Quit')
    else:       # #If the support isnt here, you cant share with the support
        print('\nA) Drink a mana potion\nB) Moderate Speed away\nC) Full Speed away\nD) Rest\nE) Status Check\nF) Quickly get the CS\nG) Greed for the CS\nI) Turn on Zed\nQ) Quit')
    choice = input('\nPlease choose your action: ')
    if choice.upper() == 'Q': # #End game if user wants to
        done = True
        continue
    elif choice.upper() == 'A':     # #if user drinks mana potion
        if mana_pots >= 1:
            print('\nYou drink a mana potion and receive 100 mana')
            mana += 100
            mana_pots -= 1
            continue
        else:
            print('You do not have enough mana potions to do that.')
            continue
    elif choice.upper() == 'B':     # #if user runs at moderate speed
        temp_distance = random.randint(10,15)
        zed_dist += temp_distance - random.randint(10,15)
        support_unhappiness += random.randint(1,2)
        print('\nYou are running away from Zed.  You are now '+str(zed_dist)+' units away from Zed')
        if random.randint (1,2) == 1: # #random event to find extra cs
            cs += random.randint(1,2)
            print('You found more CS! You now have '+str(cs)+' cs.')
        if random.randint(1,3) == 1: # #random event to find a tower
            tower = True
            print('You are now under a protective tower')
        else:
            tower = False
    elif choice.upper() == 'C':  # # if user runs at high speed
        temp_distance = random.randint(19, 24)
        zed_dist += temp_distance - random.randint(10, 15)
        support_unhappiness += random.randint(1, 3)
        print('\nYou are quickly running away from Zed.  You are now '+str(zed_dist)+' units away from Zed')
        if random.randint(1,3) == 1:   # #random event to find tower
            tower = True
            print('You are now under a protective tower')
        else:
            tower = False
    elif choice.upper() == 'D':     # #rest
        support_unhappiness = 0
        zed_dist -= random.randint(10,15)
        mana += 45
        print('\nYour support is now happy.  You have regenerated 45 mana.  You now have '+str(mana)+' mana.')
    elif choice.upper() == 'E':     # #if user does a status check, prints out status of all variables
        print('\nMana:', mana,'\nMana Potions:', mana_pots,'\nSupport Unhappiness:', support_unhappiness, '\nDistance from Zed:', zed_dist, '\nCS:' ,cs)
        if support == True:
            print('Your support is still here.')
            continue
        else:
            print('Your support is gone.')
            continue
    elif choice.upper() == 'F':     # #user quickly gets the wave, but they use mana
        temp_mana = random.randrange(130, 161, 15)
        mana -= temp_mana
        print('\nYou quickly clear the wave, but you use '+str(temp_mana)+' mana.  You now have '+str(mana)+' mana.')
        cs += random.randint(5,7)
        zed_dist -= random.randint(10,15)
    elif choice.upper() == 'G':     # #slowly greed for the wave
        cs += random.randint(5,7)
        zed_dist -= random.randint(13,17)
        print('\nYou now have '+str(cs)+' cs.')
    elif choice.upper() == 'H':     # #share the wave with the support.
        if support == True:
            cs += random.randint (2,3)
            support_unhappiness -= 5
            if support_unhappiness < 0:
                support_unhappiness = 0
            zed_dist -= random.randint(8,12)
            print("\nYou share the wave with your support.  Your support's unhappiness is now "+str(support_unhappiness)+".  You now have "+str(cs)+" cs.")
        else:
            print('You cannot share CS with your support because your support is gone.')
            continue
    elif choice.upper() == 'I':     # #turn on Zed
        zed_turn()
    else:
        print('That is not a valid response. ')

    # #random event to find a camp or a wave
    if random.randint(1,5) == 1:
        print('\nYou find a camp of raptors nearby in the jungle.  Would you like to take it? (Y/N)')
        choice = input('Enter choice here (Y/N): ')
        if choice.upper() == 'Y':
            cs += 6
            zed_dist -= random.randint(9,14)
            print('\nYou clear the raptor camp, so you receive 6 cs.  You now have '+str(cs)+' cs.')
        elif choice.upper() == 'N':
            print('\nYou did not clear the raptor camp.')
        else:
            print('\nThat is not a valid response.')
    elif random.randint(1,6) == 1:
        print('\nYou find the Scuttle Crab in the river.  Would you like to kill it?')
        choice = input('Enter choice here (Y/N): ')
        if choice.upper() == 'Y':
            cs += 4
            zed_dist -= random.randint(8,12)
            print('\nYou kill the Scuttle crab, so you receive 4 cs.  You now have '+str(cs)+' cs.')
        elif choice.upper() == 'N':
            print('\nYou did not clear the Scuttle Crab.')
        else:
            print('That is not a valid response.')

    # #ways to die
    if zed_dist <= 0:
        print('Zed has jumped onto you.')
        if flash == True:
            print('\nWould you like to turn (T) on zed? Or do you want to flash (F) away?')
            choice = input('Enter T or F to choose: ')
            if choice.upper() == 'T':
                zed_turn()
                continue
            elif choice.upper() == 'F':
                zed_dist = 18
                flash = False
                print('\nYou used your flash to escape.  You are now '+str(zed_dist)+' units away from zed')
            else:
                print('\nYou did not pick a valid response.  Zed kills you.')
                done = True
                continue
        else:
            print('You do not have flash, so you are forced to turn on Zed.')
            zed_turn()
            continue
    elif zed_dist <= 14:
        print('Zed is too close for comfort.')
        if tower == True:
            print('You are under a protective tower.')


    if support == True:     # #If the support is still there
        if support_unhappiness >= 15:       # #if he is too unhappy he is just gone
            support = False
            print('\nYou support has left you.')
        elif support_unhappiness >= 10:     # #if he is kinda unhappy he might leave
            if random.randint(1,4) == 3:
                support = False
                print('Your support has left you.')
            else:                           # #warning that he might leave
                print('Your support is unhappy.')
        elif support_unhappiness >8:
            print('Your support is unhappy.')
    else:       # #chance that the support returns
        if random.randint(1,15) == 5:
            support = True
            print('Your support has returned!')


print('\nYou finished the game with '+str(cs)+' cs.')