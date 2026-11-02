"""Python CRUD Operations Lab Sheet 09 solution."""
# Store and manage product details using CRUD operations.
products = {}

while True:
    print("\\n1.Add 2.View 3.Update 4.Delete 5.Exit")
    choice = input("Choose an option: ").strip()

    try:
        if choice == "1":
            product_id = input("Product ID: ").strip()
            if product_id in products:
                print("Product ID already exists.")
                continue
            name = input("Product name: ").strip()
            price = float(input("Price: "))
            quantity = int(input("Quantity: "))
            products[product_id] = {"name": name, "price": price,
                                     "quantity": quantity}
            print("Product added.")
        elif choice == "2":
            for product_id, details in products.items():
                print(product_id, details)
            if not products:
                print("No products found.")
        elif choice == "3":
            product_id = input("Product ID to update: ").strip()
            if product_id in products:
                products[product_id]["price"] = float(input("New price: "))
                products[product_id]["quantity"] = int(input("New quantity: "))
                print("Product updated.")
            else:
                print("Product not found.")
        elif choice == "4":
            product_id = input("Product ID to delete: ").strip()
            if products.pop(product_id, None) is None:
                print("Product not found.")
            else:
                print("Product deleted.")
        elif choice == "5":
            break
        else:
            print("Invalid choice.")
    except ValueError:
        print("Enter a valid price or quantity.")
