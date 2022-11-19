low = 1
high = 1000

print("Please think of a number between {} and {} ".format(low, high))
input("Press ENTER to start")

guesses = 1
guess = 1

while low != high:
    guesses = low + (high - low) // 2
    high_low = input("My guess is {0}. Should i guess high or lower? "
                     "Enter h or l, or c if my guess is correct"
                     .format(guesses).casefold())
    if high_low == "h":
        # Guess higher. The low end of the range becomes 1 greater than the guess.
        low = guesses + 1
    elif high_low == "l":
        # Guess lower. The high end of the range becomes one less than the guess
        high = guesses - 1
    elif high_low == "c":
        print("I got it in {} guesses".format(guess))
        break
    else:
        print("Please enter h, l or c")
    guess += 1
else:
    print("You thought of the number {}".format(low))
    print("I got it in {} guesses".format(guess))