#Chapter 6_Programming Projects #3 - Heap of Beans

'''Start with a heap of beans and two players. Each player can remove
1,2, or 3 beans from the pile of 16 or random. Each player is required
to take some number of beans from the pile during each turn. Player who takes
the last bean loses.'''

#Entry message
#Take input from both players to choose how many beans need to be taken
#Total bean count is random, 16 max 4 min

import random


def playerOne(totalBeans):
    totalBeans = totalBeans - 1
    message = f'Player One moves! total beans is {totalBeans}.'
    print(message)
    return totalBeans

def playerTwo(totalBeans):
    totalBeans = totalBeans - 1
    message = f'Player Two moves! total beans is {totalBeans}.'
    print(message)
    return totalBeans


totalBeans = 16
playerCount = 1

for i in range(0, 15):
    totalBeans = playerOne(totalBeans)
    if totalBeans == 1:
        message = f'Player {playerCount} is the loser! Player {playerCount + 1} wins!'
        print(message)
        break
    playerCount+=1
    totalBeans = playerTwo(totalBeans)
    if totalBeans == 1:
        message = f'Player {playerCount} is the loser! Player {playerCount - 1} wins!'
        print(message)
        break
    playerCount-=1

print("Thank you for playing! ")

        
