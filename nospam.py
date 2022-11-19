menu = [
    ["eggs", "bacon"],
    ["eggs", "sausage", "bacon"],
    ["eggs", "spam"],
    ["eggs", "bacon", "spam"],
    ["eggs", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "sausage", "spam", "bacon", "spam", "tomato", "spam"],
    ["spam", "eggs", "spam", "spam", "bacon", "spam"],
]
for meal in menu:
    top_index = len(meal) - 1
    for index, item in enumerate(reversed(meal)):
        if "spam" in item:
            del meal[top_index - index]
    print(meal)

for meal in menu:
    for item in meal:
        if item != "spam":
            print(item, end=', ')
    print()
