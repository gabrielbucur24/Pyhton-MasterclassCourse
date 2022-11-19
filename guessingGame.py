answer = 5

print("Please guess number between 1 and 10: ")
guess = int(input())

if guess == answer:
    print("You got it first time")
else:
    if guess > answer:
        print("Please guess lower")
    else:
        print("Please guess higher")
    guess = int(input())
    if guess == answer:
        print("Well done")
    else:
        print("You are wrong, sry")

# if guess < answer:
#     print("Please guess higher")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed it")
#     else:
#         print("Sorry, you are wrong")
# elif guess > answer:
#     print("Please guess lower")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed it")
#     else:
#         print("Sorry, you are wrong")
# else:
#     print("You got it first time!")

