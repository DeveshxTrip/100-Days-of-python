import random


t = 20
while t != 0:
    number = random.randint(1, 20)
    num = random.randint(1, 20)
    if num == number:
        print("congrats")
        break
    else:
        print(num, " ", number)
    t -= 1
