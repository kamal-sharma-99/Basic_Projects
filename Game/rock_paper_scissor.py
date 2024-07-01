import random
s='''
    Welcome To Our Rock Paper Scissors Game
                1) Rock
                2) Paper
                3) Scissor
                4) quit the game
'''
# 1 for Rock > Scissor 3
# 2 for Paper > Rock 1
# 3 for Scissor > Paper 2
status = True
while status:
    comp = random.randint(1,3)
    print(s)
    user = int(input("Enter Your Choice : "))

    if user == comp:
        print("Game Draw")
    elif comp == 1 and user == 3:
        print("Computer Won By Choosing Rock")
    elif comp == 3 and user == 1:
        print("You Won By Choosing Rock")
    elif comp == 2 and user == 1:
        print("Computer Won By Choosing Paper")
    elif comp == 1 and user == 2:
        print("You Won By Choosing Paper")
    elif comp == 3 and user == 2:
        print("Computer Won By Choosing Scissors")
    elif comp == 2 and user == 3:
        print("You Won By Choosing Scissors")

    elif user == 4:
        status = False