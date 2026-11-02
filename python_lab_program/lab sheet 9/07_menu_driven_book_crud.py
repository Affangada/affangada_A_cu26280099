"""Python CRUD Operations Lab Sheet 09 solution."""
# Menu-driven CRUD operations on a list of books.
books = []

while True:
    print("\\n1.Add Book  2.View Books  3.Update Book  4.Delete Book  5.Exit")
    choice = input("Enter choice: ").strip()

    if choice == "1":
        book_id = input("Book ID: ").strip()
        if any(b["id"] == book_id for b in books):
            print("Book ID already exists.")
            continue
        title = input("Book title: ").strip()
        author = input("Author: ").strip()
        books.append({"id": book_id, "title": title, "author": author})
        print("Book added.")
    elif choice == "2":
        if not books:
            print("No books available.")
        for book in books:
            print(book)
    elif choice == "3":
        book_id = input("Book ID to update: ").strip()
        for book in books:
            if book["id"] == book_id:
                book["title"] = input("New title: ").strip()
                book["author"] = input("New author: ").strip()
                print("Book updated.")
                break
        else:
            print("Book not found.")
    elif choice == "4":
        book_id = input("Book ID to delete: ").strip()
        for book in books:
            if book["id"] == book_id:
                books.remove(book)
                print("Book deleted.")
                break
        else:
            print("Book not found.")
    elif choice == "5":
        break
    else:
        print("Invalid choice.")
