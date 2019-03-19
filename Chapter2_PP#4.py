#Chapter 2_Programming Project - Weird Multiplication
'''You will be implementing the Russian Peasant method for multiplication.
a) Write a program to find the product of two intergers.
b) Modify your program so that it repeatedly asks whether you want to find
    another product.'''

#Entry welcome
#Part B
#Make each step visible w/ comment

enterLoop = True
numberA = int(input("What is your first integer? :"))
numberB = int(input("What is your second integer? :"))

sum = 0
while enterLoop:
    if numberB % 2 == 1:
        numberB = int(numberB/2)
        sum = sum + numberA
        numberA = numberA * 2
        if numberB == 0:
            enterLoop = False
    else:
        numberA = numberA * 2
        numberB = int(numberB/2)
        if numberB == 0:
            enterLoop = False

print("----" * 20)
print(sum)
        
