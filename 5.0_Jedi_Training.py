  #Sign your name:________________

'''
 1. Make the following program work. 
print("This program takes three numbers and returns the sum.")
'''

total = 0
for i in range(3):
     x = int(input("Enter a number: "))
     total = total + x
print("The total is:", total)

'''
  2. Write a Python program that will use a FOR loop to print the even
     numbers from 2 to 100, inclusive.
'''

for i in range(2,101,2):
    print(i)

'''
  3. Write a program that will use a WHILE loop to count from
     10 down to, and including, 0. Then print the words Blast off! Remember, use
     a WHILE loop, don't use a FOR loop.
'''


number = 10

while number >= 0:
    print(number)
    number -= 1
print('Blast Off!')


'''
  4. Write a program that prints a random integer from 1 to 10 (inclusive).
'''


import random
num = random.randint(1,11)
print(num)


'''
  5. Write a Python program that will:
     
     * Ask the user for seven numbers
     * Print the total sum of the numbers
     * Print the count of the positive entries, the count of entries equal to zero,
     and the count of negative entries. Use an if, elif, else chain, not just three
     if statements.
      
'''

total = 0
positive_count = 0
negative_count = 0
zero_count = 0

for i in range(7):
    number = int(input('Please enter a number: '))
    total += number
    if number > 0:
        positive_count += 1
    elif number < 0:
        negative_count += 1
    else:
        zero_count += 1

print('\nThe sum of all numbers is '+ str(total))
print('There were '+str(positive_count)+' positive numbers, '+str(negative_count)+' negative numbers, and '+str(zero_count)+' zeros')

'''
TURTLE.GON
'''


import turtle
number = int(input('\nHow many sides of GON do you want? '))
tom = turtle.Turtle()
tom.shape('turtle')
for i in range(number):
    tom.left(360/number)
    tom.forward(60)
turtle.Screen().exitonclick()
