""" Swap two tuples. """
tuple1 = (10, 20, 30)
tuple2 = ("A", "B", "C")
print("Before swapping:")
print("Tuple 1:", tuple1)
print("Tuple 2:", tuple2)

tuple1, tuple2 = tuple2, tuple1

print("After swapping:")
print("Tuple 1:", tuple1)
print("Tuple 2:", tuple2)
