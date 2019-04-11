#Chapter 5_Programming Project - Scrambled Words
'''Task will be to read in a paragraph from a file, scramble the internal letters
of each word, and then write the result to a file.
1) Rotate letter by 13
2) For each letter choose a random number and rotate that letter by the random amount.
    '''

import re
import random

print("This program will scramble the internal letters and write to a file.")
print("You get to choose by which rotation or random!")
#Read file
inputFile = open("Chapter5_PP#1(InputFile).txt", "r")
#Write to output file
outputFile = open("Chapter5_PP#1(OutputFile).txt", "w")

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
    #Random from 1 - 26. 26 would result in no movement
    random = random.randint(1, 26)
    print()
    print("The computer has chosen ROT" + str(random))
    shift = random

#Alphabet string used to find the correct index, once found will shift from there.
alphabet = 'abcdefghijklmnopqrstuvwxyz'
finalString = ''
newIndexNumber = 0
for line_str in inputFile:
    #Get rid of duplicate spaces in string
    stringNoDupSpaces = re.sub(' +', ' ', line_str)
    #Each word in to a list, seperated by spaces
    line_str_split = stringNoDupSpaces.split(' ')
    for word in line_str_split:
        #If length of word is more then or equal to 3
        if len(word) >= 3:
            count = 1
            #Split word into first, middle and last
            first, mid, last = word[0], word[1:-1], word[-1]
            fullWord = ''
            newMid = ''
            for i in mid:
                #At end of each word save to finalString to print
                if count == len(mid):
                    #Find letter in alphabet and save index number then shift
                    newIndexNumber = ((alphabet.index(i) + shift) % 26)
                    #Join the middle of the word after using new index.
                    newMid += alphabet[newIndexNumber]
                    #Join the whole word together
                    fullWord = first + newMid + last
                    #Add complete word to final string.
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
#Print before shift
print("BEFORE: ")
print(stringNoDupSpaces)
print()
print()
print("AFTER: ")
#Print after shift
print(finalString)
#Write to output file
outputFile.write(finalString)

#Close both files
inputFile.close()
outputFile.close()

  
            
        
        
        

