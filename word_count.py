# We need an empty dictionary, to store and display the letter frequencies.
word_count = {}

# Text string
text = "Later in the course, you'll see how to use the collections Counter class."

# Your code goes here ...
word_count = {}
count = 0
omit = (',', '.', '\'', ' ')
for char in text.casefold():
    if char not in omit:
        word_count[char] = word_count.setdefault(char, 0) + 1

# Printing the dictionary
for letter, count in sorted(word_count.items()):
    print(letter, count)
