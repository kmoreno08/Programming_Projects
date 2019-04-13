#Chapter 6_Programming Projects #3 - Heap of Beans

'''Start with a heap of beans and two players. Each player can remove
1,2, or 3 beans from the pile of 16 or random. Each player is required
to take some number of beans from the pile during each turn. Player who takes
the last bean loses.'''

#Entry message
#Take input from both players to choose how many beans need to be taken
#Total bean count is random, 16 max 4 min (user choses)
#needs to be in functions


def user_a_amount(total_beans):
    user_a_int = int(input("How many beans would you like to take user A? "))
    total_beans -= user_a_int
    print(f'{total_beans} number of bean(s) are left!')
    return total_beans

def user_b_amount(total_beans):
    user_b_int = int(input("How many beans user B? "))
    total_beans -= user_b_int
    print(f'{total_beans} number of bean(s) are left!')
    return total_beans
    
                  

import random

total_beans = 16
print("whoever takes the last bean loses!")
while True:
    total_beans = user_a_amount(total_beans)
    if total_beans <= 0:
        print("Sorry user A, you have taken the last bean!")
        print("The winner is User B.")
        break
    total_beans = user_b_amount(total_beans)
    if total_beans <= 0:
        print("Sorry user B, you have lost!")
        print("The winner is User A.")
        break


print("Have a great day!")




        
