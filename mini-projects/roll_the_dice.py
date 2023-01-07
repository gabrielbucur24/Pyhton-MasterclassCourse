import random

while True:
    print("Let's Roll the Dice!")
    print("1.Roll\t0.Exit")
    user = int(input())
    if user == 1:
        number = random.randint(1, 6)
        print(f"Dice - {number}")
    else:
        break
