"""Python Set Operations Lab Sheet 06 solution."""
first = input("Enter first string: ").replace(" ", "").lower()
second = input("Enter second string: ").replace(" ", "").lower()
if len(first) == len(second) and set(first) == set(second):
    # Set comparison alone can miss different character frequencies.
    from collections import Counter
    if Counter(first) == Counter(second):
        print("The strings are anagrams.")
    else:
        print("The strings are not anagrams.")
else:
    print("The strings are not anagrams.")
