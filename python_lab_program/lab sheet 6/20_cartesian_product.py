"""Python Set Operations Lab Sheet 06 solution."""
a = {1, 2, 3}
b = {"x", "y"}
product = {(x, y) for x in a for y in b}
print("Cartesian product A x B:", product)
