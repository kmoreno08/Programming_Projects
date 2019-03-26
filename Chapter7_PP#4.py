#Chapter 7_Programming Projet #4 - Code Breaking
'''A) Write a program that prompts for a shift value and then prompts
for plain text to encode. output the encrypted cipher text, and then decrypt
the cipher text and output that. Both should match.
B) Write a program that takes in a cipher text, determines the shift, decodes
it, and outputs the decoded message.'''

#Still completing A first
#Entry message
#Shift by user
#Use string.index(i) + shift) % 26 (Function) then join code


string = 'abcdefghijklmnopqrstuvwxyz'
print(string[0])

newMid = ""
code = []
for i in range(0, len(string)):
    count = 0
    new = ""
    #Saving string after changing all letters
    print(string[i])
    if string[i] == 'a':
            new = chr(ord(string[i]) + 13)
            newMid += new
            count+=1
    elif string[i] == 'b':
        new = chr(ord(string[i]) + 13)
        newMid += new
        count+=1
    elif string[i] == 'c':
        new = chr(ord(string[i]) + 13)
        newMid += new  
        count+=1
    elif string[i] == 'd':
        new = chr(ord(string[i]) + 13)
        newMid += new
        count+=1
    elif string[i] == 'e':
        new = chr(ord(string[i]) + 13)
        newMid += new
        
        count+=1
    elif string[i] == 'f':
        new = chr(ord(string[i]) + 13)
        newMid += new

        count+=1
    elif string[i] == 'g':
        new = chr(ord(string[i]) + 13)
        newMid += new

        count+=1
    elif string[i] == 'h':
        new = chr(ord(string[i]) + 13)
        newMid += new

        count+=1
    elif string[i] == 'i':
        new = chr(ord(string[i]) + 13)
        newMid += new

        count+=1
    elif string[i] == 'j':
        new = chr(ord(string[i]) + 13)
        newMid += new
        count+=1
    elif string[i] == 'k':
        new = chr(ord(string[i]) + 13)
        newMid += new
        count+=1
    elif string[i] == 'l':
        new = chr(ord(string[i]) + 13)
        newMid += new
        count+=1
    elif string[i] == 'm':
        new = chr(ord(string[i]) + 13)
        newMid += new
        count+=1
    elif string[i] == 'n':
        new = chr(ord(string[i]) - 13)
        newMid += new
        count+=1
    elif string[i] == 'o':
        new = chr(ord(string[i]) - 13)
        newMid += new
        count+=1
    elif string[i] == 'p':
        new = chr(ord(string[i]) - 13)
        newMid += new
        count+=1
    elif string[i] == 'q':
        new = chr(ord(string[i]) - 13)
        newMid += new
        count+=1
    elif string[i] == 'r':
        new = chr(ord(string[i]) - 13)
        newMid += new
        count+=1
    elif string[i] == 's':
        new = chr(ord(string[i]) - 13)
        newMid += new
        count+=1
    elif string[i] == 't':
        new = chr(ord(string[i]) - 13)
        newMid += new
        count+=1
    elif string[i] == 'u':
        new = chr(ord(string[i]) - 13)
        newMid += new
        count+=1
    elif string[i] == 'v':
        new = chr(ord(string[i]) - 13)
        newMid += new
        count+=1
    elif string[i] == 'w':
        new = chr(ord(string[i]) - 13)
        newMid += new
        count+=1
    elif string[i] == 'x':
        new = chr(ord(string[i]) - 13)
        newMid += new
        count+=1
    elif string[i] == 'y':
        new = chr(ord(string[i]) - 13)
        newMid += new
        count+=1
    elif string[i] == 'z':
        new = chr(ord(string[i]) - 13)
        newMid += new
        count+=1
    else:
        newMid += mid[i]
count+=1
print(newMid)
