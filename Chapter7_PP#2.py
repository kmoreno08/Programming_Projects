#Chapter 7_Programming Project #2 - Pascal's Triangle
'''Write a program that prompts for the height of Pascal's triangle'''

#Put in functions
#Welcome message

#List of all rows combined
#Create the correct spacing


print("How many rows of Pascals Triangle would you like to see? (Max 6 )")
num_rows = int(input("Please enter here: "))
row0 = [0, 1 , 0]

row1 = []
#rowCount = 1
count = 0
#row count + 2 for length of range
#Note - Range = row number + 3
for index in range(0, 4):
    #Add 0 at the Beginning and ending of list
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
    #Add 0 at the Beginning and ending of list
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
    #Add 0 at the Beginning and ending of list
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
    #Add 0 at the Beginning and ending of list
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
    #Add 0 at the Beginning and ending of list
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


#Add all lists
all_rows = []
all_rows.append(row0)
all_rows.append(row1)
all_rows.append(row2)
all_rows.append(row3)
all_rows.append(row4)
all_rows.append(row5)
    


'''#Print rows
current_row = []
full_list = []
for n in range(0,num_rows):
    current_row = all_rows[n]
    full_list = current_row + '\n' + full_list
    print(full_list)'''
    





