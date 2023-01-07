sample_list = ["abc", "xyz", "aba", "1221"]
counter = 0

for item in sample_list:
    if (len(item) >= 2) and (item[0] == item[-1]):
        counter += 1
print(counter)
