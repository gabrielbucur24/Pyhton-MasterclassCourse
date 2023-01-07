def common(str1: list, str2: list) -> bool:
    for item in str1:
        if item in str2:
            return True
    return False


list1 = [1, 2, 3, 4, 5, 6]
list2 = [0, 9, 8, 7]

print(common(list1, list2))
