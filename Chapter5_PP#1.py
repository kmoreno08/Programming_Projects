#Chapter 5_Programming Project - Scrambled Words
'''Task will be to read in a paragraph from a file, scramble the internal letters
of each word, and then write the result to a file.
1) Rotate letter by 13
2) For each letter choose a random number and rotate that letter by the random amount.
    '''

#Need Entry message
#Need to get rid of all punctuation
#Need to rotate letters (ROT13)
#Need to rotate letters (Random)
#Have user choose ROT13 or Random
#**Need to be able to change mid**
#**(first, rotateMid, last).joined together
#Print to output file


import re
input_file = open("Chapter5_PP#1(InputFile).txt", "r")
output_file = open("Chapter5_PP#1(OutputFile).txt", "w")



for line_str in input_file:
    #Get rid of duplicate spaces in string
    stringNoDupSpaces = re.sub(' +', ' ', line_str)
    #Each word in to a list, seperated by spaces
    line_str_split = stringNoDupSpaces.split(' ')
    for word in line_str_split:
        print("word " + word)
        #Small word does not need to be changed
        if len(word) >= 3:
            #Split word into first, middle and last
            first, mid, last = word[0], word[1:-1], word[-1]
            emptyString = ''
            new = ''
            count = 1
            print("Top Mid " + mid)
            print(emptyString)
            for i in range(0, len(mid)):
                emptyString = emptyString + new
                print(emptyString)
                #if i == len(mid)-1:
                    #mid = emptyString
                    #print("This is mid empty!!" + mid)
                    #break
                if count == len(mid):
                    mid = emptyString
                    print(mid + " from if statement")
                elif mid[i] == 'a':
                    new = chr(ord(mid[i]) + 13)
                    count+=1
                elif mid[i] == 'b':
                    new = chr(ord(mid[i]) + 13)
                    count+=1
                elif mid[i] == 'c':
                    new = chr(ord(mid[i]) + 13)
                    count+=1
                elif mid[i] == 'd':
                    new = chr(ord(mid[i]) + 13)
                    count+=1
                elif mid[i] == 'e':
                    new = chr(ord(mid[i]) + 13)
                    count+=1
                elif mid[i] == 'f':
                    new = chr(ord(mid[i]) + 13)
                    count+=1
                elif mid[i] == 'g':
                    new = chr(ord(mid[i]) + 13)
                    count+=1
                elif mid[i] == 'h':
                    new = chr(ord(mid[i]) + 13)
                    count+=1
                elif mid[i] == 'i':
                    new = chr(ord(mid[i]) + 13)
                    count+=1
                elif mid[i] == 'j':
                    new = chr(ord(mid[i]) + 13)
                    count+=1
                elif mid[i] == 'k':
                    new = chr(ord(mid[i]) + 13)
                    count+=1
                elif mid[i] == 'l':
                    new = chr(ord(mid[i]) + 13)
                    count+=1
                elif mid[i] == 'm':
                    new = chr(ord(mid[i]) + 13)
                    count+=1
                elif mid[i] == 'n':
                    new = chr(ord(mid[i]) - 13)
                    count+=1
                elif mid[i] == 'o':
                    new = chr(ord(mid[i]) - 13)
                    count+=1
                elif mid[i] == 'p':
                    new = chr(ord(mid[i]) - 13)
                    count+=1
                elif mid[i] == 'q':
                    new = chr(ord(mid[i]) - 13)
                    count+=1
                elif mid[i] == 'r':
                    new = chr(ord(mid[i]) - 13)
                    count+=1
                elif mid[i] == 's':
                    new = chr(ord(mid[i]) - 13)
                    count+=1
                elif mid[i] == 't':
                    new = chr(ord(mid[i]) - 13)
                    count+=1
                elif mid[i] == 'u':
                    new = chr(ord(mid[i]) - 13)
                    count+=1
                elif mid[i] == 'v':
                    new = chr(ord(mid[i]) - 13)
                    count+=1
                elif mid[i] == 'w':
                    new = chr(ord(mid[i]) - 13)
                    count+=1
                elif mid[i] == 'x':
                    new = chr(ord(mid[i]) - 13)
                    count+=1
                elif mid[i] == 'y':
                    new = chr(ord(mid[i]) - 13)
                    count+=1
                elif mid[i] == 'z':
                    new = chr(ord(mid[i]) - 13)
                    count+=1
                '''count = 0
                if 
                if ord(letter) > 96 and ord(letter) < 110:
                    newLetter = chr(ord(letter) + 13)
                    letter = newLetter
                    
                else:
                    newLetter = chr(ord(letter) - 13)
                    letter = newLetter
                    print("2 " + letter)
            print(mid)
            
    

  
            
        
        
        

