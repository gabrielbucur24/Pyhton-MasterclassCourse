def palindrome_sentence(sentence):
    """
    Checks if the String sentence is a palindrome.

    The function checks for any non-alphabetical characters.
    :param sentence: The string that will be tested
    :return: Returns boolean value True if palindrome is found,
        False otherwise
    """
    string = ""
    for char in sentence:
        if char.isalnum():
            string += char
    # print(string)
    return string[::-1].casefold() == string.casefold()


def is_palindrome(word):
    """
    Checks if the String is a palindrome.

    The function fill return True of False.
    :param word: The string that will be tested
    :return: Boolean value
    """
    if word.isalpha():
        return word[::-1].casefold() == word.casefold()
    else:
        return False


expression = input("Enter your word/sentence to be tested if is a palindrome:")

if palindrome_sentence(expression):
    print("{0} is palindrome".format(expression))
else:
    print("'{}' is not a palindrome".format(expression))


# print(convert_to_string("This is just a test, amazing!"))
# print(is_palindrome_sentence("This is another test, wow!"))
