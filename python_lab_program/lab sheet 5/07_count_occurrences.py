""" Count occurrences of an element in a tuple. """
my_tuple = (10, 20, 10, 30, 10, 40, 20)
item = int(input("Enter the element to count: "))
print("Occurrences of", item, ":", my_tuple.count(item))
