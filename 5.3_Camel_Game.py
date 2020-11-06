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
import time

done = False
cs = 0
mana_pots = 2
mana = 550
support_unhappiness = 0
zed_dist = random.randint(25, 28)
support = True
tower = False
turn = 0
flash = True

def zed_turn():
    global turn
    global done

    print('\nYou try to turn and kill Zed')
    if support == False:  # # If there is no support, then it will subtract 50% chance from final calculation
        calc_support = 50
    else:
        calc_support = 0
    if tower == True:  # # If under tower, plus 30% chance
        calc_tower = 30
    else:
        calc_tower = 0
    if mana <= 150:  # # if less than 150 mana, then subtract 25% chance
        calc_mana = 25
    else:
        calc_mana = 0
    turn = (random.randint(cs - 10, cs + 25) - calc_support + calc_tower - calc_mana) / 100

    for i in range(1,4):
        b = "Calculating" + "." * i
        print("\r", b, end="")
        time.sleep(.75)

    if turn >= 1: # # if the turn is sucessful, then kill zed and win the game
        print('\n\nYou sucessfully kill Zed!  You win!')
        print('\n[All] Oogabooga23 (Zed): adc diff')
    if turn < 1:
        print('\n\nYou were not strong enough, so Zed killed you.  Try getting more CS next time.')
    done = True


# # Instructions on how to play the game
print('\nWelcome to league of legends!  You made a mistake coming here.')
print("Today you will be playing an ADC, which means you need CS (minion kills) in order to do anything. Focus on farming and don't get killed.")
print('The mid lane assassin is Zed, and he is coming to kill you.  Make sure you keep enough distance from him.  About 20-30 units away is ideal.')
print('Make sure you keep your support happy, they can leave you.')
print('Mana can be used to get cs faster, but make sure you have enough.')
print('In order to win, you must gather lots of cs so you can do damage, then you can turn and kill Zed.')

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
            mana += 100
            mana_pots -= 1
            print('\nYou drink a mana potion and receive 100 mana.  You now have '+str(mana)+' mana.')
            continue
        else:
            print('You do not have enough mana potions to do that.')
            continue
    elif choice.upper() == 'B':     # #if user runs at moderate speed
        temp_distance = random.randint(10,15)
        zed_dist += random.randint(3, 4)
        support_unhappiness += 1
        print('\nYou are running away from Zed.  You are now '+str(zed_dist)+' units away from Zed')
        if random.randint (1,3) == 1: # #random event to find extra cs
            cs += random.randint(1, 2)
            print("You randomly 'found' more CS! You now have "+str(cs)+" cs. The top laner is not happy.")
        if random.randint(1,3) == 1: # #random event to find a tower
            tower = True
            print('You are now under a protective tower')
        else:
            tower = False
    elif choice.upper() == 'C':  # # if user runs at high speed
        zed_dist += random.randint(8, 12)
        support_unhappiness += random.randint(1, 2)
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
            print('Your support is here.')
            continue
        else:
            print('Your support is gone.')
            continue
    elif choice.upper() == 'F':     # #user quickly gets the wave, but they use mana
        if mana >= 160:
            temp_mana = random.randrange(115, 146, 15)
            mana -= temp_mana
            support_unhappiness += 1
            print('\nYou quickly clear the wave, but you use '+str(temp_mana)+' mana.  You now have '+str(mana)+' mana.')
            cs += random.randint(5,7)
            zed_dist -= random.randint(10,14)
            print('\nYou now have '+str(cs)+' cs.')
        else:
            print('You do not have enough mana to do that.')
            continue
    elif choice.upper() == 'G':     # #slowly greed for the wave
        cs += random.randint(5,7)
        zed_dist -= random.randint(13,17)
        support_unhappiness += 1
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
        continue
    else:
        print('That is not a valid response. ')

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
                print('\nYou used your flash to escape.  You are now ' + str(zed_dist) + ' units away from zed')
            elif choice.upper() == 'D':
                print("\nFlash goes on F, but I'll let you get away this time.")
                zed_dist = 18
                flash = False
                print('\nYou used your flash to escape.  You are now ' + str(zed_dist) + ' units away from zed')
            else:
                print('\nYou did not pick a valid response.  Zed kills you.')
                done = True
                continue
        else:
            print('\nYou do not have flash, so you are forced to turn on Zed.')
            zed_turn()
            continue
    elif zed_dist <= 16:
        print('Zed is too close for comfort.')
        if tower == True:
            print('You are under a protective tower.')

    # #random event to find a camp, cs, or a mana potion
    if random.randint(1,6) == 1 and tower == False:
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
    elif random.randint(1,8) == 1 and tower == False:
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
    elif random.randint(1,4) == 1 and tower == True:
        print('\nYou find a wave in mid lane.  Would you like to steal it? (Y/N)')
        choice = input('Enter choice here (Y/N): ')
        if choice.upper() == 'Y':
            cs += random.randint(5,7)
            zed_dist -= random.randint(9,14)
            print('\nYou now have '+str(cs)+' cs.')
        elif choice.upper() == 'N':
            print('\nYou did not take the mid wave.')
        else:
            print('\nThat is not a valid response.')
    elif random.randint(1,8) == 1:
        mana_pots += 1
        print('You found a mana potion!')


    if support == True:     # #If the support is still there
        if support_unhappiness >= 16:       # #if he is too unhappy he is just gone
            support = False
            print('\nYou support has left you.')
        elif support_unhappiness >= 12:     # #if he is kinda unhappy there is a chance that he leaves
            if random.randint(1,4) == 1:
                support = False
                print('Your support has left you.')
            else:                           # #warning that he might leave
                print('Your support is unhappy.')
        elif support_unhappiness > 8:
            print('Your support is unhappy.')
    else:       # #chance that the support returns
        if random.randint(1,18) == 1:
            support = True
            support_unhappiness = 0
            print('Your support has returned!')

print('\nYou finished the game with '+str(cs)+' cs.')
