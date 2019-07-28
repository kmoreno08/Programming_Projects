'''By using the random module, python can do things like pseudo-random number generation.
So in this program, allow the user to input the amount of sides on a dice and how many times
it should be rolled. From there, your program should simulate dice rolls and keep track of how many times each number comes up (this does not have to be displayed).
After that, print out how many times each number came up.

Sub-Goals:
1)Adjust your program so that if the user does not type in a number when they need to, the program will keep prompting them to type in a real number until they do so.

2)Put the program into a loop so that the user can continue to simulate dice rolls without having to restart the entire program.

3)In addition to printing out how many times each side appeared, also print out the percentage it appeared.
If you can, round the percentage to 4 digits total OR two decimal places.'''


import random
import collections


count = 1
#Empty list
result = []


#Keep asking user until positive numbers are the input
while True: 
    try:
        #Ask user how many sides the dice should be
        input_sides = int(input("How many sides would you like on the dice? "))
        #Positive numbers only
        if input_sides < 1:
            input_sides = 1
        #How many times they would like to roll the dice
        input_roll = int(input("How many times would you like to roll the die? "))
        #Positive Numbers only
        if input_roll < 1:
            input_roll = 1
        break
    except:
        print("That is not the correct input, Please try again! ")
        print("Needs to be a real number.")

#Roll as many times as needed
while count != (input_roll + 1):
    #Create a random number from 1 to number of sides
    random_int = random.randint(1,input_sides)
    #Add number to result list
    result.append(random_int)
    #Increase count
    count += 1

#Counter sets dictionary for items
counter = collections.Counter(result)

print("The total number of sides picked are :")
#Print counter
print(counter)
    








