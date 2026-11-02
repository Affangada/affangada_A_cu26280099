""" Find the length of the longest word in a tuple. """
words = ("Python", "Programming", "MCA", "Computer", "Science")
longest_word = max(words, key=len)
print("Words:", words)
print("Longest word:", longest_word)
print("Length of longest word:", len(longest_word))
