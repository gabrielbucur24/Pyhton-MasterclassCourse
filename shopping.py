shopping_list = ["milk", "pasta", "eggs", "spam", "rice"]

# for item in shopping_list:
#     if item != "spam":
#         print("Buy " + item)

# for item in shopping_list:
#     if item == "spam":
#         continue
#     print("Buy " + item)

item_to_find = "spam"
found_at = None

for ind in range(len(shopping_list)):
    if shopping_list[ind] == item_to_find:
        found_at = ind
        break
print("item found at position {}".format(found_at+1))