numbers = input("Please enter 3 numbers separated by a ',': ").split(",")
# numbers = numbers.split(",")

for index in range(len(numbers)):
    numbers[index] = int(numbers[index])
a, b, c = numbers
result = a + b - c
print(result)
