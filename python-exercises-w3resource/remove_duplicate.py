sample_list = ["abc", "xyz", "abc", "spam", "spam", "key"]

for item in sample_list:
    for index in sample_list:
        if item in sample_list:
            sample_list.remove(item)
            if item not in sample_list:
                sample_list.append(item)

print(sample_list)
