""" Find the index of an element in a tuple. """
my_tuple = (10, 20, 30, 40, 50)
item = int(input("Enter the element: "))

if item in my_tuple:
    print("Index of", item, "is", my_tuple.index(item))
else:
    print("Element not found in the tuple.")
