animals = {'Turtle',
           'Horse',
           'Robin',
           'Python',
           'Swallow',
           'Hedgehog',
           'Wren',
           'Aardvark',
           'Cat',
           }
birds = {'Robin', 'Swallow', 'Wren'}

print(f"birds is a subset o animals: {birds.issubset(animals)}")
print(f"animals is a superset of birds: {animals.issuperset(birds)}")
