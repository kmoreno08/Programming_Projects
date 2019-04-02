#Chapter 2_Programming Project - How thick does paper folding get?
'''What would be the thickness of a piece of paper if it was folded 30 times?
Assume the paper is 1/200cm thick. Write a program to solve this puzzle.
Prompt for the number of folds and output the thickness in meters.'''


print("Welcome! This program will calculate how thick a piece of paper gets after a certain amount of folds.")

numberOfFolds = int(input("How many folds would you like to do? "))
paperThickness = 1/200

#totalThickness = paperThickness * numberOfFolds
count = 1
#For loop to count number of folds
for i in range(0, numberOfFolds):
    totalThick = paperThickness * count
    count = count + 1
message = f'The total thickness is {totalThick} with {numberOfFolds} number of folds.'
print(message)
