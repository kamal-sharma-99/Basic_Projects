import random
s = "Welcome To Our Number Guessing Game"
print(s)
status = True
guess = random.randint(1,100)
count=0
while status:
    count+=1
    user = int(input("Guess Your Number : "))
    if guess == user:
        print("You Won")
        print(f"You Took {count} Chances To Win")
        status = False
    elif guess > user:
        print("Try Bigger")
    elif guess < user:
        print("Try Lower")