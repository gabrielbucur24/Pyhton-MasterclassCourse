from contents import pantry, recipes

# display_dict = {str(index + 1): meal for index, meal in enumerate(recipes)}


def add_items_to_list(data: dict, item: str, amount: int) -> None:
    # if item in data:
    #     data[item] += amount
    # else:
    #     data[item] = amount
    data[item] = data.setdefault(item, 0) + amount


to_buy_list = {}
display_dict = {}

for index, key in enumerate(recipes):
    display_dict[str(index + 1)] = key

while True:
    # Display menu of the recipes we know how to cook
    print("Please choose your recipe")
    print("-------------------------")
    for key, value in display_dict.items():
        print(f"{key} - {value}")
    choice = input(": ")
    if choice == "0":
        break
    elif choice in display_dict:
        selected_item = display_dict[choice]
        print(f"You have selected {selected_item}")
        print("checking ingredients...")
        ingredients = recipes[selected_item]
        print(ingredients)
        for food_item, required_quantity in ingredients.items():
            quantity_in_pantry = pantry.get(food_item, 0)
            if required_quantity <= quantity_in_pantry:
                print(f"\t{food_item} OK")
            else:
                quantity_to_buy = required_quantity - quantity_in_pantry
                # print(f"\tYou need to buy {quantity_to_buy} of {food_item}")
                # to_buy_list[food_item] = quantity_to_buy
                add_items_to_list(to_buy_list, food_item, quantity_to_buy)

print("You need to buy the following ingredients: ")
for key, value in to_buy_list.items():
    print(key, value, sep=" - ")

