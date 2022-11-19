import random

highest = 10
answer = random.randint(1, highest)
print(answer)
guess = int(input("Please guess number between 1 and {}: ".format(highest)))

while guess != answer:
    if guess > answer:
        print("Guess lower")
    else:
        print("Guess higher")
    guess = int(input())
if guess == answer:
    print("Well done, you got it")

# if guess == answer:
#     print("You got it first try")
# else:
#     if guess < answer:
#         print("Guess higher")
#     else:
#         print("Guess lower")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed it")
#     else:
#         print("Sorry, you are wrong")