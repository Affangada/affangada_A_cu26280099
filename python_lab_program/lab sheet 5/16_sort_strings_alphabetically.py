""" Sort a tuple of strings alphabetically. """
words = ("Mango", "Apple", "Orange", "Banana", "Grapes")
sorted_words = tuple(sorted(words, key=str.lower))
print("Original tuple:", words)
print("Alphabetical order:", sorted_words)
