#Chapter 7_Programming Project #2 - Pascal's Triangle
'''Write a program that prompts for the height of Pascal's triangle'''

#Put in functions
#Welcome message
#Get user input and make the triangle scalable
#List of all rows combined
#Create the correct spacing

    
row0 = [0, 1 , 0]

row1 = []
#rowCount = 1
count = 0
#row count + 2 for length of range
#Note - Range = row number + 3
for index in range(0, 4):
    if index == 0 or index == 3:
        row1.append(int(0))
        count+=1
    else:
        firstCalc = row0[index]
        secondCalc = row0[index - 1]
        totalCalc = firstCalc + secondCalc
        row1.append(totalCalc)
        count+=1
        
count = 0
row2 = []
for index in range(0, 5):
    print(index)
    if index == 0 or index == 4:
        row2.append(int(0))
        count+=1
    else:
        firstCalc = row1[index]
        secondCalc = row1[index - 1]
        totalCalc = firstCalc + secondCalc
        row2.append(totalCalc)
        count+=1

count = 0
row3 = []
for index in range(0, 6):
    #Note - Length = number of row + 1
    #Note - index[-1] = length - 1
    if index == 0 or index == 5:
        row3.append(int(0))
        count+=1
    else:
        #Note - current row - 1
        firstCalc = row2[index]
        secondCalc = row2[index - 1]
        totalCalc = firstCalc + secondCalc
        row3.append(totalCalc)
        count+=1

count = 0
row4 = []
for index in range(0, 7):
    #Note - Length = number of row + 1
    #Note - index[-1] = length - 1
    if index == 0 or index == 6:
        row4.append(int(0))
        count+=1
    else:
        #Note - current row - 1
        firstCalc = row3[index]
        secondCalc = row3[index - 1]
        totalCalc = firstCalc + secondCalc
        row4.append(totalCalc)
        count+=1

count = 0
row5 = []
for index in range(0, 8):
    #Note - Length = number of row + 1
    #Note - index[-1] = length - 1
    if index == 0 or index == 7:
        row5.append(int(0))
        count+=1
    else:
        #Note - current row - 1
        firstCalc = row4[index]
        secondCalc = row4[index - 1]
        totalCalc = firstCalc + secondCalc
        row5.append(totalCalc)
        count+=1

print("---" * 20)
print(row0)
print(row1)
print(row2)
print(row3)
print(row4)
print(row5)



