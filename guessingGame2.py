import random


def get_integer(prompt):
    """
    Get an integer from Standard Input (stdin).

    The function will continue looping and prompting
    the user, until a valid `int` is entered.

    :param prompt: The String that the user will see, when
        they're prompted to enter the value.
    :return: The integer that the user enters.
    """
    while True:
        temp = input(prompt)
        if temp.isnumeric():
            return int(temp)
        # else:
        print("'{}' is not a valid number! Try again".format(temp))     # else not needed


highest = 10
answer = random.randint(1, highest)
print(answer)
guess = 0
print("Please guess number between 1 and {}".format(highest), end=' ')

while guess != answer:
    guess = get_integer(": ")
    if guess > answer:
        print("Guess lower")
    else:
        print("Guess higher")
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