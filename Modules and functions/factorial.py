def fact(n):
    """ calculate n! iteratively """
    result = 1
    if n > 1:
        for f in range(2, n + 1):
            result *= f
    return result


def factorial(n):
    """ calculate n! recursively """
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)


print(fact(3))
print(factorial(3))
