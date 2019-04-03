#What is the invention of chess worth?

'''
The local ruler was so pleased with the invention that he offered
the inventor a great reward in gold. The inventor suggested an
alternative reward: he would get one grain of wheat on the first square,
two grains on the second square, four on the third, eight on the fourth. Board
has 64 sqaures. Write a program to determine the following:
 (a) How many total grains of wheat did the ruler have to pay the inventor?
 (b) A wheat grain weighs approximately 50 mg. How much did the wheat weigh?
'''



print("A local ruler was pleased with the invention of chess that he offered gold.")
print("The inventor suggested an alternative reward: he would get on grain of wheat")
print("on the first square, two grains on the second square, four on the third and so on.")
print()
print("This program will determine how many total grain of wheat did the ruler have to pay the inventor")
print("and how much did that wheat weight in miligrams.")
print()

#Excercise A
sum = 1
count = 2
mult = 2
#For loop to find amount of grain
for i in range(1,65):
    sum = sum + (mult)
    mult = mult * 2
    count = count + 1

message = f'The total grains of wheat is 36,893,488,147,419,103,231'
print(message)

#Excercise B
totalGrain = 36_893_488_147_419_103_231
weightPerGrainMG = 50
totalGrainWeightMG = weightPerGrainMG * totalGrain
print("Total weight in miligrams is " + str(totalGrainWeightMG))


    

