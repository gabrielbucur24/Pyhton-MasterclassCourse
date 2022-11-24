def palindrome_sentence(sentence):
    string = ""
    for char in sentence:
        if char.isalnum():
            string += char
    print(string)
    return string[::-1].casefold() == string.casefold()


def is_palindrome(word):
    if word.isalpha():
        return word[::-1].casefold() == word.casefold()
    else:
        return False


expression = "This is just a test, amazing!"
print(palindrome_sentence(expression))


# print(convert_to_string("This is just a test, amazing!"))
# print(is_palindrome_sentence("This is another test, wow!"))
