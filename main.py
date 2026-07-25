from mylibrary import Library


def menu():
    lib = Library()
    while True:
        print("\n===== Library Management System =====")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. Search Book")
        print("4. Show All Books")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            lib.add_book(title, author)
        elif choice == "2":
            title = input("Enter book title to remove: ")
            lib.remove_book(title)
        elif choice == "3":
            title = input("Enter book title to search: ")
            lib.search_book(title)
        elif choice == "4":
            lib.show_books()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    menu()
