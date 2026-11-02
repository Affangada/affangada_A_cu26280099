""" Find common elements between two tuples. """
tuple1 = (10, 20, 30, 40, 50)
tuple2 = (30, 40, 60, 70)
common = tuple(item for item in tuple1 if item in tuple2)
print("Tuple 1:", tuple1)
print("Tuple 2:", tuple2)
print("Common elements:", tuple(dict.fromkeys(common)))
