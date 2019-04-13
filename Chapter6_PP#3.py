#Chapter 6_Programming Projects #3 - Heap of Beans

'''Start with a heap of beans and two players. Each player can remove
1,2, or 3 beans from the pile of 16 or random. Each player is required
to take some number of beans from the pile during each turn. Player who takes
the last bean loses.'''

#Entry message

def player_choice():
    print("Would you like to have a random choice of beans (min: 4, max: 16) or")
    print("have 16 beans in total?")
    player_choice = input("Random? (Please type y/n) : ")
    player_choice = player_choice.lower()
    #If yes, then total beans are a random number
    if player_choice == 'y':
        total_beans = random
        print(f'Random has been chosen! You have {total_beans} beans in total.')
        return total_beans
    #Total beans are 16
    else:
        total_beans = 16
        print("You have 16 total beans!")
        return total_beans
    
def user_a_amount(total_beans):
    user_a_int = int(input("How many beans would you like to take user A? "))
    total_beans -= user_a_int
    print(f'{total_beans} bean(s) are left!')
    return total_beans

def user_b_amount(total_beans):
    user_b_int = int(input("How many beans user B? "))
    total_beans -= user_b_int
    print(f'{total_beans} bean(s) are left!')
    return total_beans
    
                  

import random
#Random number from 4 to 16
random = random.randint(4, 16)

#User chooses random or 16 total beans
total_beans = player_choice()

print("whoever takes the last bean loses!")
#While loop to keep asking user until all beans are gone
while True:
    #User A takes a turn
    total_beans = user_a_amount(total_beans)
    #User A loses if takes last bean
    if total_beans <= 0:
        print("Sorry user A, you have taken the last bean!")
        print("The winner is User B.")
        break
    #User B takes a turn
    total_beans = user_b_amount(total_beans)
    #User B loses if takes last bean
    if total_beans <= 0:
        print("Sorry user B, you have lost!")
        print("The winner is User A.")
        break


print("Have a great day!")




        
