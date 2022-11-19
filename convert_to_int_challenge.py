generated_list = ['9', ' ',
                  '2', '2', '3', ' ',
                  '3', '7', '2', ' ',
                  '0', '3', '6', ' ',
                  '8', '5', '4', ' ',
                  '7', '7', '5', ' ',
                  '8', '0', '7',
                  ]

values = "".join(generated_list)
values_list = values.split()
numbers_list = []
for number in values_list:
    numbers_list.append(int(number))
print(numbers_list)


