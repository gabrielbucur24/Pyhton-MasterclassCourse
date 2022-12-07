from math import pi


# Calculate the area of a circle
radius = int(input("Enter the radius of your circle: "))

area = pi * pow(radius, 2)
print(f"The area of your circle is {area}")

values = input("Enter numbers separated by ',': ")
list_1 = values.split(",")
tuple_1 = tuple(list_1)
print(list_1, tuple_1)

