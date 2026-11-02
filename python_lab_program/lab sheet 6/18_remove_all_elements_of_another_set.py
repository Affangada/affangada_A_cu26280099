"""Python Set Operations Lab Sheet 06 solution."""
a = {1, 2, 3, 4, 5}
b = {3, 4}
a.difference_update(b)
print("A after removing all elements of B:", a)
