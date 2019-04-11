#Chapter 5_Programming Project - Scrambled Words
'''Task will be to read in a paragraph from a file, scramble the internal letters
of each word, and then write the result to a file.
1) Rotate letter by 13
2) For each letter choose a random number and rotate that letter by the random amount.
    '''

#Need Entry message
#Need to rotate letters (Random)
#Have user choose ROT13 or Random
#Print to output file
#If length of word is less than 3, need to add to completeString



import re
input_file = open("Chapter5_PP#1(InputFile).txt", "r")
output_file = open("Chapter5_PP#1(OutputFile).txt", "w")

alphabet = 'abcdefghijklmnopqrstuvwxyz'
completeString = ''
shift = 13
newIndexLetter = 0
for line_str in input_file:
    #Get rid of duplicate spaces in string
    stringNoDupSpaces = re.sub(' +', ' ', line_str)
    #Each word in to a list, seperated by spaces
    line_str_split = stringNoDupSpaces.split(' ')
    for word in line_str_split:
        print("word --------" + word)
        #Small word does not need to be changed
        if len(word) >= 3:
            count = 1
            #Split word into first, middle and last
            first, mid, last = word[0], word[1:-1], word[-1]
            fullWord = ''
            newMid = ''
            for i in mid:
                #Try/Except for characters that are not letters
                try:
                    newIndexLetter = ((alphabet.index(i) + shift) % 26)
                    newMid += alphabet[newIndexLetter]
                    count += 1
                except ValueError:
                    newMid += i
                    count += 1
                if count == len(mid):
                    newIndexLetter = ((alphabet.index(i) + shift) % 26)
                    newMid += alphabet[newIndexLetter]
                    print("The End")
                    fullWord = first + newMid + last
                    print(fullWord)
                    completeString += fullWord + " "
                    print("THE END!")
            print(completeString)


print()
print("---" * 20)
print(stringNoDupSpaces)
print()
print()
print(completeString)

  
            
        
        
        

