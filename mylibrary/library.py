class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        book = {"title": title, "author": author}
        self.books.append(book)
        print(f"Book '{title}' by {author} added successfully.")

    def remove_book(self, title):
        for book in self.books:
            if book["title"].lower() == title.lower():
                self.books.remove(book)
                print(f"Book '{title}' removed successfully.")
                return
        print(f"Book '{title}' not found.")

    def search_book(self, title):
        found = [
            book for book in self.books
            if title.lower() in book["title"].lower()
        ]
        if found:
            print(f"\nSearch results for '{title}':")
            for book in found:
                print(f"  - {book['title']} by {book['author']}")
        else:
            print(f"No book found with title '{title}'.")
        return found

    def show_books(self):
        if not self.books:
            print("No books in the library.")
        else:
            print("\n--- All Books ---")
            for i, book in enumerate(self.books, 1):
                print(f"{i}. {book['title']} by {book['author']}")
            print(f"\nTotal books: {len(self.books)}")
