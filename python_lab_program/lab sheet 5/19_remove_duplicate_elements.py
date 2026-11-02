""" Remove duplicate elements from a tuple. """
my_tuple = (10, 20, 10, 30, 20, 40, 30)
unique_tuple = tuple(dict.fromkeys(my_tuple))
print("Original tuple:", my_tuple)
print("Tuple without duplicates:", unique_tuple)
