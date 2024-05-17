# Snake Water Gun Project 

import random


def gameWin(computer , you):
    
    # if two values are equal, declare a tie!
    
    if computer == you:
        return None
    
    # check for all possibilities when computer chose s
    
    elif computer == 's':
        if you == 'w':
            return False
        elif you == 'g':
            return True
    
   # check for all possibilities when computer chose w 
    
    elif computer == 'w':
        if you == 'g':
            return False
        elif you == 's':
            return True
    
    # check for all possibilities when computer chose g
    
    elif computer == 'g':
        if you == 's':
            return False
        elif you == 'w':
            return True
        
        
print("computer turn: Snake(s) Water(w) or Gun(g)?: ")
 
# As we already imported random module so we can use this module here to chose a random number between 1-3 by the help of inbuilt function (randint)
 
randomNO = random.randint(1 , 3) # randint is a inbulit function in random module

if randomNO == 1:
    computer = 's'
    
elif randomNO == 2:
    computer = 'w'

elif randomNO == 3:
    computer = 'g' 
    
you = input("your turn: Snake(s) Water(w) or Gun(g)?: ")                   

a = gameWin(computer , you)

print(f"computer chose {computer}")
print(f"you chose {you}")

if a == None:
    print("The game is tie!")

elif a:
    print("You Win!")    
 
else:
    print("You Lose!")    
    