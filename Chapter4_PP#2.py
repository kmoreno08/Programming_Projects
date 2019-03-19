#Chapter 4_Programming Project #2 - Mad Libs
'''You are prompted for categories of words and then those words are inserted
into a predifined story. The predefined story has placeholders for those
words that get replaced by the values prompted for.'''



#Entry Message
#Keep asking user - While loop
#Fix replace

adjOne = input("Please enter an adjective. : ")
nounOne = input("Plese enter a noun. : ")
adjTwo = input("Please enter another adjective. : ")
nounTwo = input("Please enter another noun. : ")
adjThree = input("Please enter the last adjective. : ")
nounThree = input("Please enter the last noun. : ")
girlName = input("Please enter a girls name. : ")

story = "Once upon a time in the middle of a ADJECTIVE_ONE NOUN_ONE stood a \
ADJECTIVE_TWO NOUN_TWO, the home of a ADJECTIVE_ONE ADJECTIVE_THREE \
NOUN_THREE known to everyone as GIRLS_NAME"


print(adjOne)

print(story.replace(adjOne, "ADJECTIVE_ONE"))

