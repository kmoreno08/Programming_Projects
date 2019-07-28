#Hangman Game
''' Game to guess the word.
 1) The user needs to be able to input letter guesses.
 2) A limit should also be set on how many guesses they can use.
 3) Keep notifying the user of the remaining turns.
Text file will be used for words. There will also be a check if the user has actually inputed
a single letter, to check if the input is in the hidden word (and if it is, how many times
it appears), to print letters, and a count variable to limit guesses.
'''

#Text file of words from "dwyl" on Github 466k words - https://github.com/dwyl/english-words
import random


#Intro
print("Welcome to Hangman!")
print("You will try to guess the word by inputing each letter.")
print("Remember, All letters are lower case!")

#User chooses how many guesses
while True:
    try:
        guesses_left = int(input("How many guesses would you like? Max(30): "))
        #Max the guesses to 30
        if guesses_left > 30:
            guesses_left = 30
        break
    #Has to be an integer
    except:
        print("That's not a valid option!")


#Empty list
word_list = []

#All words in document in to a list
with open("hangman_text.txt") as file:
    for word in file:
        word_list.append(word)

#Random number for length of list
random_num = random.randrange(1,len(word_list))

#Pick word by random 
word = word_list[random_num]

#Lower case the word
word_lower = word.lower()


#Make word in to a list
list_word = list(word_lower)


#remove '/n' 
list_word = list_word[:-1]
print(list_word)
len_list_word = len(list_word)
print(len_list_word)

#Program will exit if no guesses left
while guesses_left != 0:
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
            #Remaining length of word
            len_list_word -= 1
            #Iterate through each letter in word
            for letter in list_word:
                #Letter is in word then remove from list
                if letter == user_letter:
                    list_word.remove(letter)
                    print(list_word)
            print("Remaining number of guesses left are " + str(guesses_left))
            print("Remaining characters that have to be guessed are " + str(len_list_word))
        #Letter is not in word   
        else:
            print("nope, sorry!")
            guesses_left -= 1
            #Remaining length of word
            print("Remaining characters that have to be guessed are " + str(len_list_word))
            print("Remaining number of guesses left are " + str(guesses_left))
       #If guess all letters in word
    print("Congrats! You have guessed the word!")
    print("The word is " + word)
    guesses_left = 0
#Exit program    
print("You have exited the program.")
