import random
import time
operators = ["+", "-", "*"]
min_num = 3
max_num = 12
total_problems = 10

def generate_problem():
    left = random.randint(min_num, max_num)
    right = random.randint(min_num, max_num)
    operator = random.choice(operators)

    expr = str(left) + " " + operator + " " + str(right)
    answer = eval(expr)
    return expr, answer

wrong = 0
input("Press Enter To Start!")
print("---------------------")

start_time = time.time()

for i in range(total_problems):
    expr, answer = generate_problem()
    while True:
        guess = input("Problem #" + str(i+1) + ": " + expr + " = ")
        if guess == str(answer):
            break
        wrong += 1

end_time = time.time()
total_time = round(end_time - start_time, 2)
print("----------------------")
print(f"Nice wrok you finished in {total_time} seconds")