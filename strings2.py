number = input("Please enter a series of numbers, using any "
               "using any separator you like: ")
separators = ""

for char in number:
    if not char.isnumeric():
        separators += char

values = "".join(char if char not in separators else " " for char
                 in number).split()
print(sum([int(val) for val in values]))