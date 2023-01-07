
sample_list = ["Red", "Green", "White", "Black", "Pink", "Yellow"]
colors = []
for i, x in enumerate(sample_list):
    if i not in (0, 4, 5):
        colors.append(x)

print(colors)
