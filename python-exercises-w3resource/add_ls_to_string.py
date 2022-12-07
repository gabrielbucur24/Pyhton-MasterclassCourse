ls = "ls"

your_string = input("Enter your string: ").casefold()

if your_string[:2] == "ls":
    print(your_string)
else:
    ls += your_string
    print(ls)
