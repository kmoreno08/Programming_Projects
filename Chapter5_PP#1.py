#Chapter 5_Programming Project - Scrambled Words
'''Task will be to read in a paragraph from a file, scramble the internal letters
of each word, and then write the result to a file.
1) Rotate letter by 13
2) For each letter choose a random number and rotate that letter by the random amount.
    '''

#Need Entry message
#Print to output file




import re
import random
input_file = open("Chapter5_PP#1(InputFile).txt", "r")
output_file = open("Chapter5_PP#1(OutputFile).txt", "w")

print("Would you like to choose the rotation of letters, if so type 'y'")
print("Or would you like the computer to choose randomly. If so type 'n'")

shift = 0
#User choice for random or choose the shift
userChoice = input("'y' for user choice or 'n' for random. Please type here : ")
print("--" * 20)
if userChoice == 'y':
    userInputShift = int(input("How much of a shift in letters would you like? : "))
    shift = userInputShift
    print("You have chosen a shift of " + str(shift))
else:
    random = random.randint(1, 26)
    print()
    print("The computer has chosen ROT" + str(random))
    shift = random


alphabet = 'abcdefghijklmnopqrstuvwxyz'
finalString = ''
newIndexLetter = 0
for line_str in input_file:
    #Get rid of duplicate spaces in string
    stringNoDupSpaces = re.sub(' +', ' ', line_str)
    #Each word in to a list, seperated by spaces
    line_str_split = stringNoDupSpaces.split(' ')
    for word in line_str_split:
        #if len(word) >= 3:
        if len(word) >= 3:
            count = 1
            #Split word into first, middle and last
            first, mid, last = word[0], word[1:-1], word[-1]
            fullWord = ''
            newMid = ''
            for i in mid:
                #At end of each word save to finalString to print
                if count == len(mid):
                    newIndexLetter = ((alphabet.index(i) + shift) % 26)
                    newMid += alphabet[newIndexLetter]
                    fullWord = first + newMid + last
                    finalString += fullWord + " "
                #Try/Except for characters that are not letters
                try:
                    newIndexLetter = ((alphabet.index(i) + shift) % 26)
                    newMid += alphabet[newIndexLetter]
                    count += 1
                except ValueError:
                    newMid += i
                    count += 1
        #words with less than length of three, add to finalString w/out shift.
        else:
            finalString += word + " "


print()
print("BEFORE: ")
print(stringNoDupSpaces)
print()
print()
print("AFTER: ")
print(finalString)

  
            
        
        
        

