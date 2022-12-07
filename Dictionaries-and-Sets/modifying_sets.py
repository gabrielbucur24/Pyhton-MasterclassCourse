numbers = set()
print(numbers, type(numbers))

# numbers.add("cow")
# print(numbers)
#
# while len(numbers) < 4:
#     next_values = int(input("Please enter your next value: "))
#     numbers.add(next_values)
# print(numbers)

data = ["blue", "red", "blue", "green", "red", "blue", "white"]

# Create a set from a list, to remove duplicates

unique_data = set(data)
print(unique_data)

# Create a list of unique colours, keeping the order they appeared

unique_data = list(dict.fromkeys(data))
print(unique_data)

