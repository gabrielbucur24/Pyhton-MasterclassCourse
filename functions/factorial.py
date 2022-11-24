def factorial(n: int) -> int:
    """
    Calculate factorial.
    :param n: The stop point of factorial
    :return: Factorial result
    """
    if n == 0:
        return 1
    n *= factorial(n - 1)
    return n


for i in range(36):
    print(i, factorial(i))
