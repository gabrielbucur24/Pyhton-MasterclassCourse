def fizz_buzz(num):
    if (num % 3 == 0) and (num % 5 == 0):
        return "fizz buzz"
    elif num % 3 == 0:
        return "fizz"
    elif num % 5 == 0:
        return "buzz"


for i in range(100):
    print(fizz_buzz(i))