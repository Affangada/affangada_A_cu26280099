"""Python Set Operations Lab Sheet 06 solution."""
s = {10, 20, 30, 40}
x = int(input("Enter element to search: "))
if x in s:
    print(x, "exists in the set.")
else:
    print(x, "does not exist in the set.")
