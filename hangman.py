#Hangman Game
''' Game to guess the word.
 1) The user needs to be able to input letter guesses.
 2) A limit should also be set on how many guesses they can use.
 3) Keep notifying the user of the remaining turns.
Text file will be used for words. There will also be a check if the user has actually inputed
a single letter, to check if the inputted is in the hidden word (and if it is, how many times
it appears), to print letters, and a count variable to limit guesses.
'''

#Text file of words from "dwyl" on Github - 466k words
import random

print("Welcome to Hangman")
print("Please guess a letter")
print("All letters are lower case.")
guesses_left = int(input("How many guesses would you like? "))





#Empty list
word_list = []

#Read text document to grab word by Random
file = open("hangman_text.txt", "r")


for word in file:
    word_list.append(word)

random_num = random.randrange(1,len(word_list))
word = word_list[random_num]
word_lower = word.lower()



#Make word in to a list
list_word = list(word_lower)

#Program will exit if no guesses left
while guesses_left != 0:
    #If guess all letters in word
    print("Congrats! You have guessed the word!")
    print("The word is " + word)
    while list_word != []:
        #Break out of loop if no guesses left
        if guesses_left == 0:
            print("You have no remaing guesses left!")
            print("Letter(s) that have still not been guessed: " + str(list_word))
            print("The whole word is : " + word)
            break
        #Keep asking for letter
        print("Please enter a letter: ")
        user_letter = input("Enter letter : ")
        #Check if letter is in word
        if user_letter in list_word:
            print("Yes it is in here")
            guesses_left -= 1
            #Iterate through each letter in word
            for letter in list_word:
                #Letter is in word then remove from list
                if letter == user_letter:
                    list_word.remove(letter)
                    print(list_word)
            print("Your remaining number of guesses are " + str(guesses_left))
        #Letter is not in word   
        else:
            print("nope, sorry!")
            guesses_left -= 1
            print("Your remaining number of guesses are " + str(guesses_left))

#Exit program    
print("You have exited the program.")
