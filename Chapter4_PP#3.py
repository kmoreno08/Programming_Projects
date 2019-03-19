#Chapter#3_Programming Project - Pig Latin
'''Pig Latin is a game of alterations played on words. To make the Pig Latin form
of an English word the initial consonant sound is transposed to the end of
the words and an "ay" is affixed. Specifically there are two rules:
(a) If a word begins with a vowel, append "yay" to the end of the word.
(b)If a word begins with a consonant, remove all the consonants from
    the beginning up to the first vowel and append them to the end of the word.
    Finally, append "ay" to the end of the word.
Write a program that repeatedly prompts for an english word to translate
into Pig Latin and prints the translated word. If the user enters a period,
halt the program.'''

#Entry Message
#User exit "."
userWord = input("Which word would you like to translate in to Pig Latin?: ")
vowels = 'aeiou'
vowelFirst = "yay"
vowelConst = "ay"
empty = ""
if userWord[0] in vowels:
    newWord = userWord + vowelFirst
    print(newWord)
else:
    for i in userWord:
        if i in vowels:
            userWord = userWord + vowelConst
            print("User word is " + userWord)
            break
        empty = userWord[0]
        print("Empty " + empty)
        userWord = userWord[1:]
        print("User Word after move " + userWord)
        userWord = userWord + empty
        print("Together User word " + userWord)
    
