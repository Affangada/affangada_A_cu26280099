"""Python Set Operations Lab Sheet 06 solution."""
s = {10, 20, 30, 40}
s.discard(50)  # No error even if the element is absent
print("Set after discard:", s)
