def fizz_buzz(num: int) -> str:
    """
    Playing the Fizz Buzz.
    :param num:The `int` that will be checked
    :return:The string that represents the number
    """
    if (num % 3 == 0) and (num % 5 == 0):
        return "fizz buzz"
    elif num % 3 == 0:
        return "fizz"
    elif num % 5 == 0:
        return "buzz"
    else:
        return str(num)


response = ""
contor = 1

input("Play Fizz Buzz.     Press ENTER to start")
print()

while contor <= 100:
    if contor % 2 == 0:
        print("Computer says: {}".format(fizz_buzz(contor)))
    else:
        response = input("Your go : ")
        if response != fizz_buzz(contor):
            print("You just lost, I'm sorry... NOT")
            break
    contor += 1
else:
    print("Congratulations!")

# for i in range(100):
#     print(fizz_buzz(i))
