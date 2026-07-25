# mylibrary - Python Library Management System

[![PyPI](https://img.shields.io/pypi/v/mylibrary.svg)](https://pypi.org/project/mylibrary/)

A simple and elegant Python library management system for organizing and tracking books.

## Features

- **Add Books**: Store book titles and authors
- **Remove Books**: Delete books from the library
- **Search Books**: Search by title (partial matches)
- **Show All Books**: View entire collection with statistics

## Installation

Install via pip:

```bash
pip install mylibrary
```

For local development from this repository:

```bash
pip install .
```

## Usage

### Basic Usage

```python
from mylibrary import Library

lib = Library()
lib.add_book("Python Crash Course", "Eric Matthes")
lib.add_book("Clean Code", "Robert Martin")

lib.show_books()
# 1. Python Crash Course by Eric Matthes
# 2. Clean Code by Robert Martin
# Total books: 2

lib.search_book("python")
# Search results for 'python':
#   - Python Crash Course by Eric Matthes

lib.remove_book("Clean Code")

lib.show_books()
# 1. Python Crash Course by Eric Matthes
# Total books: 1
```

### Interactive Menu

Run the interactive CLI menu directly:

```bash
python3 main.py
```

Use menu options to:
1. Add a book
2. Remove a book
3. Search for a book
4. Show all books
5. Exit

## API

### Library

| Method | Description | Parameters | Returns |
|--------|-------------|------------|---------|
| `add_book(title, author)` | Add a book to the library | `title` (str), `author` (str) | None |
| `remove_book(title)` | Remove a book from the library | `title` (str) | None |
| `search_book(title)` | Search books by title | `title` (str) | List of matching books |
| `show_books()` | Display all books in the library | None | None |

## Examples

### Web Framework

```python
from mylibrary import Library

lib = Library()

# Add a collection of books
books = [
    ("The Pragmatic Programmer", "David Thomas"),
    ("Effective Python", "Brett Slatin"),
    ("Clean Architecture", "Robert Martin"),
]

for title, author in books:
    lib.add_book(title, author)

# Find and catalog all Martin books
martin_books = [b for b in lib.books if b["author"] == "Robert Martin"]
print(f"Robert Martin books: {len(martin_books)}")
```

### CLI Integration

```python
from mylibrary import Library

import argparse
def main():
    lib = Library()
    parser = argparse.ArgumentParser(description="Add a book")
    parser.add_argument("title", help="Book title")
    parser.add_argument("author", help="Book author")

    args = parser.parse_args()
    lib.add_book(args.title, args.author)
    lib.show_books()
if __name__ == "__main__":
    main()
```

## Development

### Running Tests

Tests can be added in the future:

```bash
pytest
```

### Project Structure

```
library/
├── mylibrary/
│   ├── __init__.py
│   └── library.py
├── setup.py
├── main.py
├── README.md
└── .gitignore
```

## License

MIT

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run tests
5. Submit a pull request

## Issues

Found a bug or have a feature request? Please open an issue in this repository.

## Changelog

### 1.0.0

- Initial release
- Core functionality added

## Special Thanks

This project was created as part of Python learning and best practices demonstration.