""" Check whether an element exists in a tuple. """
my_tuple = (10, 20, 30, 40, 50)
item = int(input("Enter the element to search: "))

if item in my_tuple:
    print(item, "exists in the tuple.")
else:
    print(item, "does not exist in the tuple.")
