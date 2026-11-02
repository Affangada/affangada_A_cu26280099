""" Flatten a nested tuple. """
nested_tuple = ((1, 2), (3, 4), (5, 6))
flat_tuple = tuple(item for sub_tuple in nested_tuple for item in sub_tuple)
print("Nested tuple:", nested_tuple)
print("Flattened tuple:", flat_tuple)
