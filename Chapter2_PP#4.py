#Chapter 2_Programming Project - Weird Multiplication
'''You will be implementing the Russian Peasant method for multiplication.
a) Write a program to find the product of two intergers.
b) Modify your program so that it repeatedly asks whether you want to find
    another product.'''


#Entry message
print("Welcome to the russian peasant method for multiplication.")
print("This program will show each step and what process took place.")
print("To exit: type 'exit' at anytime.")
print()
#Loop to keep asking user for input
while True:
    innerLoop = True
    numberA = input("What is your first integer? : ")
    numberA = numberA.lower()
    #exit program by user
    if str(numberA) == 'exit':
        break
    numberA = int(numberA)
    numberB = input("What is your second integer? : ")
    numberB = numberB.lower()
    #exit program by user 
    if str(numberB) == 'exit':
        break
    numberB = int(numberB)
   #Zero sum, empty comment and message for table
    sum = 0
    comment = ""
    message = ""
    print("__" * 21)
    #Headline
    print(f'{"A":>5}|{"B":>5}|{"Comment":<30}|')
    while innerLoop:
        #If B is odd
        if numberB % 2 == 1:
            #If B is zero, exit inner loop to print answer
            if numberB == 0:
                break
            comment = "Add A to the product, B is odd"
            #Table
            message = f'{numberA:>5}|{numberB:>5}|{comment:<20}|'
            print(message)
            #Calculation if B is odd
            numberB = int(numberB/2)
            sum = sum + numberA
            numberA = numberA * 2
        else:
            #exit inner loop to print answer
            if numberB == 0:
                break
            comment = "Ignore this A value, B is even"
            #Table
            message = f'{numberA:>5}|{numberB:>5}|{comment:<20}|'
            print(message)
            #Calculation if B is even
            numberA = numberA * 2
            numberB = int(numberB/2)
    #Answer
    print("__" * 21)
    print("Your total is " + str(sum))
    print("**" * 21)

#Exit message
print("Thank you for trying the Russian method multiplication calculator.")   
print("Have a great day!")
