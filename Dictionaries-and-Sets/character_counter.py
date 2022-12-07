# We need an empty dictionary, to store and display the letter frequencies.
word_count = {}

# Text string
text = "Later in the course, you'll see how to use the collections Counter class."
# Your code goes here ...

for letter in text.casefold():
    count = 0
    if letter.isalnum():
        for i in range(0, len(text)):
            if text[i].casefold() == letter.casefold():
                count += 1
        word_count[letter] = count
# Printing the dictionary
for letter, count in sorted(word_count.items()):
    print(letter, count)
