import random
from datetime import datetime

score = 0
x_range = int(input("What range for X? "))
y_range = int(input("What range for Y? "))
start = input("Press any key to begin.")
questions = 0
count = 0


while count < 20:
    x = random.randint(1, x_range)
    y = random.randint(1, y_range)
    operator = random.randint(1, 5)
    if operator == 1:
        response = input(' ' + str(x) + " * " + str(y) + ' = ')
        answer = str(x*y)
        if response == answer:
            print("Correct!")
            score += 1
        else:
            print("Wrong, it's " + answer)
    elif operator == 2:
        response = input(' ' + str(x) + " + " + str(y) + ' = ')
        answer = str(x+y)
        if response == answer:
            print("Correct!")
            score += 1
        else:
            print("Wrong, it's " + answer)
    elif operator == 3:
        response = input(' ' + str(x * y) + " / " + str(y) + ' = ')
        answer = str(x)
        if response == answer:
            print("Correct!")
            score += 1
        else:
            print("Wrong, it's " + answer)
    elif operator == 4:
        response = input(" Sqrt(" + str(x * x) + ') = ')
        answer = str(x)
        if response == answer:
            print("Correct!")
            score += 1
        else:
            print("Wrong, it's " + answer)
    else:
        response = input(' ' + str(x) + " - " + str(y) + ' = ')
        answer = str(x-y)
        if response == answer:
            print("Correct!")
            score += 1
        else:
            print("Wrong, it's " + answer)
    count += 1
    if count == 20:
        print("Final Score is " + str(score) + " out of 20.")
f = open("scores.txt", "a+")
f.write(str(datetime.now()) + " " + str(score) + "/20\r\n")
start = input("Press any key to close.")
