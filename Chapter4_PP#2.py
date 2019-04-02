#Chapter 4_Programming Project #2 - Mad Libs
'''You are prompted for categories of words and then those words are inserted
into a predifined story. The predefined story has placeholders for those
words that get replaced by the values prompted for.'''


def exit_program(input):
    lower_input = input.lower()
    if lower_input == "exit":
        exit = False
        return False
    
        #print("Function")
        #print(exit)
        #return exit

def original_message():
    print('''Once upon a time in the middle of a ADJECTIVE_ONE NOUN_ONE stood a\
    ADJECTIVE_TWO NOUN_TWO, the home of a ADJECTIVE_ONE ADJECTIVE_THREE\
    NOUN_THREE known to everyone as GIRLS_NAME''')
    
    

print("Welcome to the Mad Libs generator!")
print("This is your original message. ")
print("---" * 20)
original_message()
print("---" * 20)
print("Please enter your word when prompted.")
print("To exit the program please type 'exit' at anytime.")

#Keep asking user - While loop
#Put in Function
#How to exit with function

exit_program = True
while exit_program:
    print(exit_program)
    #All users inputs needed
    adjOne = input("Please enter an adjective. : ")
    exitProgram(adjOne)
    print(exit)
    nounOne = input("Plese enter a noun. : ")
    adjTwo = input("Please enter another adjective. : ")
    nounTwo = input("Please enter another noun. : ")
    adjThree = input("Please enter the last adjective. : ")
    nounThree = input("Please enter the last noun. : ")
    girlName = input("Please enter a girls name. : ")
    #Original message
    original = '''Once upon a time in the middle of a ADJECTIVE_ONE NOUN_ONE stood a\
    ADJECTIVE_TWO NOUN_TWO, the home of a ADJECTIVE_ONE ADJECTIVE_THREE\
    NOUN_THREE known to everyone as GIRLS_NAME'''
    #Adjective #1
    replaceAdjOne = '''Once upon a time in the middle of a ADJECTIVE_ONE
    '''.replace('ADJECTIVE_ONE', adjOne)
    #Noun # 1
    replaceNounOne = "NOUN_ONE stood a ".replace('NOUN_ONE', nounOne)
    #Adjective #2
    replaceAdjTwo = "ADJECTIVE_TWO ".replace('ADJECTIVE_TWO',adjTwo)
    #Noun #2
    replaceNounTwo = "NOUN_TWO, the home of a ".replace('NOUN_TWO', nounTwo)
    #Adjective #1
    replaceAdjOneSelf = "ADJECTIVE_ONE ".replace("ADJECTIVE_ONE ",adjOne)
    #Adjective #3
    replaceAdjThree = " ADJECTIVE_THREE ".replace('ADJECTIVE_THREE', adjThree)
    #Noun #3
    replaceNounThree = "NOUN_THREE known to everyone as ".replace("NOUN_THREE",nounThree)
    #Girls name
    replaceGirlName = "GIRLS_NAME".replace("GIRLS_NAME",girlName)

    #Replaced original message with user inputs
    replaceOriginal = f'{replaceAdjOne}{replaceNounOne}{replaceAdjTwo}{replaceNounTwo}{replaceAdjOneSelf}{replaceAdjThree}{replaceNounThree}{replaceGirlName}'
    print(replaceOriginal)


