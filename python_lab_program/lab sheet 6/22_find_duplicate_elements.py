"""Python Set Operations Lab Sheet 06 solution."""
items = [10, 20, 10, 30, 20, 40, 10]
seen = set()
duplicates = set()
for item in items:
    if item in seen:
        duplicates.add(item)
    else:
        seen.add(item)
print("List:", items)
print("Duplicate elements:", duplicates)
