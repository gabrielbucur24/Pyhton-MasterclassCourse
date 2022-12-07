vowels = "aeiou"

while True:
    letter = input("Enter a letter: ").casefold()
    if len(letter) > 1:
        print("Too many letters..")
        continue
    if letter == '0':
        print("Exiting...")
        break
    if letter.isalpha():
        if letter in vowels:
            print("This letter is a vowel!")
        else:
            print("This letter is a consonant..")
    else:
        print("Sir, this is not even a letter!")



