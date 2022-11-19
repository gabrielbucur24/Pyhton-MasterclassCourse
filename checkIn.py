parrot = "Norwegian Blue"

letter = input("Please enter a letter: ")

if letter in parrot:
    print("{} is in {}".format(letter, parrot))
else:
    print("I dont need that letter")

activity = input("What would you like to do today?")

if "cinema" not in activity.casefold():
    print("But i want to go to cinema")