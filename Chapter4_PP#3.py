#Chapter 4_Programming Project #3 - Pig Latin
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


print("Welcome, this program will change any word to Pig Latin.")
print("If you want to exit the application please enter '.' only")
while True:
    userWord = input("Which word would you like to translate in to Pig Latin? '.' to Exit : ")
    if userWord == ".":
        break
    vowels = 'aeiou'
    vowelFirst = "yay"
    vowelConst = "ay"
    empty = ""
    print("Your orignial word is : " + userWord)
    if userWord[0] in vowels:
        newWord = userWord + vowelFirst
        print(newWord)
    else:
        for i in userWord:
            if i in vowels:
                userWord = userWord + vowelConst
                print('The word in pig lating is : '  + userWord)
                break
            empty = userWord[0]
            userWord = userWord[1:]
            userWord = userWord + empty
            

print("Have a great day!")
        
