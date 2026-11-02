""" Find the difference between two tuples. """
tuple1 = (10, 20, 30, 40, 50)
tuple2 = (30, 40, 60)
difference = tuple(item for item in tuple1 if item not in tuple2)
print("Tuple 1:", tuple1)
print("Tuple 2:", tuple2)
print("Elements in Tuple 1 but not in Tuple 2:", difference)
