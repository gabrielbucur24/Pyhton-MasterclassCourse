def multiply(x, y):
    result = x * y
    return result


def is_palindrome(string):
    # backwards = string[::-1]
    # return backwards == string
    return string[::-1].casefold() == string.casefold()


answer = multiply(10, 4.5)
print(answer)

twenty = multiply(4, 5)
print(twenty)

print()

for val in range(1, 5):
    two_times = multiply(2, val)
    print(two_times)

word = "Racecar"
print("{0} = {1}".format(word, is_palindrome(word)))
