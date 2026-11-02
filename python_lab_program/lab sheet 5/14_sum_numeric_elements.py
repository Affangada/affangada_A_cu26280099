""" Calculate the sum of numeric elements in a tuple. """
my_tuple = (10, "Python", 20.5, 30, "MCA", 4.5)
total = sum(item for item in my_tuple if isinstance(item, (int, float)) and not isinstance(item, bool))
print("Tuple:", my_tuple)
print("Sum of numeric elements:", total)
