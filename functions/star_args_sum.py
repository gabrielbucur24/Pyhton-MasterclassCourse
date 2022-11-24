def sum_numbers(*args: float) -> float:
    """
    Calculate the sum of the specified numbers.
    :param args: Collection of numbers.
    :return: SUm of the numbers.
    """
    suma = 0
    for i in args:
        suma += i
    return suma


