"""
Q3: Library Management System
Demonstrates classes, inheritance, polymorphism, and encapsulation.
"""


class BookNotAvailableError(Exception):
    """Raised when trying to borrow a book that isn't available."""


class BookNotBorrowedError(Exception):
    """Raised when trying to return a book that wasn't borrowed by that member."""


class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self._available = True  # "protected" convention -> encapsulation

    @property
    def available(self):
        return self._available

    def mark_borrowed(self):
        self._available = False

    def mark_returned(self):
        self._available = True

    def display_info(self):
        status = "Available" if self._available else "Borrowed"
        return f"[Book] '{self.title}' by {self.author} (ISBN: {self.isbn}) - {status}"

    def __repr__(self):
        return f"Book({self.title!r}, {self.author!r}, {self.isbn!r})"


class EBook(Book):
    """An EBook is a Book with an extra file_size_mb attribute (inheritance)."""

    def __init__(self, title, author, isbn, file_size_mb):
        super().__init__(title, author, isbn)
        self.file_size_mb = file_size_mb

    def display_info(self):
        # Polymorphism: overrides Book.display_info with extra details.
        base = super().display_info()
        return f"{base} | {self.file_size_mb} MB download"


class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def __str__(self):
        return f"Member({self.name}, id={self.member_id})"


class Library:
    def __init__(self):
        self._books = {}  # isbn -> Book
        self._members = {}  # member_id -> Member

    def add_book(self, book):
        self._books[book.isbn] = book

    def add_member(self, member):
        self._members[member.member_id] = member

    def borrow_book(self, member, isbn):
        book = self._books.get(isbn)
        if book is None:
            raise KeyError(f"No book with ISBN {isbn}")
        if not book.available:
            raise BookNotAvailableError(f"'{book.title}' is already borrowed.")
        book.mark_borrowed()
        member.borrowed_books.append(book)

    def return_book(self, member, isbn):
        book = self._books.get(isbn)
        if book is None or book not in member.borrowed_books:
            raise BookNotBorrowedError(
                f"{member.name} did not borrow ISBN {isbn}."
            )
        book.mark_returned()
        member.borrowed_books.remove(book)

    def list_available_books(self):
        # Polymorphism in action: we don't check whether it's a Book or EBook,
        # we just call display_info() and the right version runs.
        for book in self._books.values():
            if book.available:
                print(" ", book.display_info())


def main():
    library = Library()
    library.add_book(Book("Clean Code", "Robert C. Martin", "111"))
    library.add_book(EBook("Fluent Python", "Luciano Ramalho", "222", file_size_mb=8.4))
    library.add_book(Book("The Pragmatic Programmer", "Hunt & Thomas", "333"))

    alice = Member("Alice", "M1")
    library.add_member(alice)

    print("Available books before borrowing:")
    library.list_available_books()

    library.borrow_book(alice, "222")
    print("\nAvailable books after Alice borrows 'Fluent Python':")
    library.list_available_books()

    try:
        library.borrow_book(alice, "222")
    except BookNotAvailableError as e:
        print(f"\nExpected error: {e}")

    library.return_book(alice, "222")
    print("\nAvailable books after returning:")
    library.list_available_books()


if __name__ == "__main__":
    main()
