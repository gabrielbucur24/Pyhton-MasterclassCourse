from contents import recipes


def dict_deep_copy(d: dict) -> dict:
    dict_copy = {}
    for key, values in d.items():
        new_values = values.copy()
        dict_copy[key] = new_values
    return dict_copy


recipes_copy = dict_deep_copy(recipes)
# print(recipes_copy)
recipes_copy["Butter chicken"]["ginger"] = 300
print(recipes_copy["Butter chicken"]["ginger"])
print(recipes["Butter chicken"]["ginger"])
