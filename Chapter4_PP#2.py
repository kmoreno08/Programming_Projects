#Chapter 4_Programming Project #2 - Mad Libs
'''You are prompted for categories of words and then those words are inserted
into a predifined story. The predefined story has placeholders for those
words that get replaced by the values prompted for.'''


def entry_message():
    print("Welcome to the Mad Libs generator!")
    print("Please enter your word when prompted.")
    print("To exit the program please type 'exit' at anytime.")
    print("This is your original message. ")
    print("---" * 20)
    
def mad_lib_message():
    print('''Once upon a time in the middle of a ADJECTIVE_ONE NOUN_ONE stood a
    ADJECTIVE_TWO NOUN_TWO, the home of a ADJECTIVE_ONE ADJECTIVE_THREE
    NOUN_THREE known to everyone as GIRLS_NAME.''')

def mad_lib_replaced(adj_one, noun_one, adj_two, noun_two,
                     adj_three, noun_three, girls_name):
    mad_lib_replaced = f'''Once upon a time in the middle of {adj_one} {noun_one} stood a
{adj_two} {noun_two}, the home of a {adj_one} {adj_three}
{noun_three} known to everyone as {girls_name}.'''
    return mad_lib_replaced


entry_message()
mad_lib_message()

#Empty strings
adj_one = ""
noun_one = ""
adj_two = ""
noun_two = ""
adj_three = ""
noun_three = ""
girls_name = ""

while True:
    #If not all 7 values are reached, will exit program.
    try:
        print("To exit: input less than 7 values. ")
        #All users inputs in list comprehension
        adj_one, noun_one, adj_two, noun_two, adj_three, noun_three, girls_name = [x for x in input("Please enter 7 values seperated by space: ").split()]
    except:
        print("Not all 7 values were put in correctly, exiting program.")
        break

    mad_lib_replaced = mad_lib_replaced(adj_one, noun_one, adj_two, noun_two,
                     adj_three, noun_three, girls_name)
    print("__" * 20)
    print(mad_lib_replaced)
    print("**" * 20)
                                        
print("Have a great day!")

