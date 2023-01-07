text = """Education is not the learning of facts
but the training of the mind to think

– Albert Einstein"""

prepositions = {"as", "but", "by", "down", "for", "in", "of", "on", "to", "with"}

# Add your code here.
words_set = set(text.split())
print(words_set)
preps_used = prepositions.intersection(words_set)

print(preps_used)

