"""Python Set Operations Lab Sheet 06 solution."""
s = frozenset([10, 20, 30, 20])
print("Frozen set:", s)
print("Length:", len(s))
print("Is 20 present?", 20 in s)
print("Union with {30, 40}:", s.union({30, 40}))
# A frozenset is immutable; add() and remove() are not supported.
