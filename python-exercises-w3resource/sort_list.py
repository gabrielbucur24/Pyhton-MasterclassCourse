def last(n):
    return n[-1]


sample_list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

sample_list = sorted(sample_list, key=last)

print(sample_list)





