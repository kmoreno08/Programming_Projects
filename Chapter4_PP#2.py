#Chapter 4_Programming Project #2 - Mad Libs
'''You are prompted for categories of words and then those words are inserted
into a predifined story. The predefined story has placeholders for those
words that get replaced by the values prompted for.'''



#Entry Message
#Keep asking user - While loop
#Put in Function


adjOne = input("Please enter an adjective. : ")
nounOne = input("Plese enter a noun. : ")
adjTwo = input("Please enter another adjective. : ")
nounTwo = input("Please enter another noun. : ")
adjThree = input("Please enter the last adjective. : ")
nounThree = input("Please enter the last noun. : ")
girlName = input("Please enter a girls name. : ")

original = '''Once upon a time in the middle of a ADJECTIVE_ONE NOUN_ONE stood a\
ADJECTIVE_TWO NOUN_TWO, the home of a ADJECTIVE_ONE ADJECTIVE_THREE\
NOUN_THREE known to everyone as GIRLS_NAME'''

replaceAdjOne = '''Once upon a time in the middle of a ADJECTIVE_ONE
'''.replace('ADJECTIVE_ONE', adjOne)

replaceNounOne = "NOUN_ONE stood a ".replace('NOUN_ONE', nounOne)

replaceAdjTwo = "ADJECTIVE_TWO ".replace('ADJECTIVE_TWO',adjTwo)
replaceNounTwo = "NOUN_TWO, the home of a ".replace('NOUN_TWO', nounTwo)

replaceAdjOneSelf = "ADJECTIVE_ONE ".replace("ADJECTIVE_ONE ",adjOne)

replaceAdjThree = " ADJECTIVE_THREE ".replace('ADJECTIVE_THREE', adjThree)
replaceNounThree = "NOUN_THREE known to everyone as ".replace("NOUN_THREE",nounThree)

replaceGirlName = "GIRLS_NAME".replace("GIRLS_NAME",girlName)


replaceOriginal = f'{replaceAdjOne}{replaceNounOne}{replaceAdjTwo}{replaceNounTwo}{replaceAdjOneSelf}{replaceAdjThree}{replaceNounThree}{replaceGirlName}'

print(replaceOriginal)


