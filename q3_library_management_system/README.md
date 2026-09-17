# Q3: Library Management System (OOP)

## Question
Design a small library management system using object-oriented programming:
1. A base class `Book` with attributes `title`, `author`, `isbn`, and `available` (bool), and a method `display_info()`.
2. A subclass `EBook` that inherits from `Book` but adds a `file_size_mb` attribute and overrides `display_info()` to show the extra info (polymorphism).
3. A `Member` class with a `name`, `member_id`, and a list of borrowed books.
4. A `Library` class that holds a collection of books and members, and supports:
   - `add_book(book)`
   - `borrow_book(member, isbn)` — marks the book unavailable and adds it to the member's borrowed list (raises an error if it's already unavailable)
   - `return_book(member, isbn)` — marks it available again and removes it from the member's list
   - `list_available_books()` — prints info for all available books (using polymorphism, calling `display_info()` on each without caring whether it's a `Book` or `EBook`)

## Approach
1. Model real-world entities as classes, with `Book` as the general case and `EBook` as a specialization — this demonstrates **inheritance**.
2. Use `super().__init__()` in `EBook` to reuse the parent constructor instead of duplicating code.
3. Override `display_info()` in `EBook` to demonstrate **polymorphism** — the `Library` can call `display_info()` on any book-like object and get the correct behavior automatically, without any `isinstance` checks.
4. Keep `available` behind a property and only change it through methods (`mark_borrowed` / `mark_returned`) rather than letting external code flip the flag directly — a simple form of **encapsulation**.
5. Use `__repr__` for developer-friendly printing.
6. Use custom exceptions to enforce business rules (you can't borrow a book that's already checked out, or return one you never borrowed).

## Concepts Used
- Classes and objects, `__init__` constructors
- Inheritance and `super()`
- Polymorphism (method overriding, duck typing)
- Encapsulation via properties/methods instead of direct attribute mutation
- Dunder methods (`__repr__`, `__str__`)
- Custom exceptions for invalid operations
- Working with collections (dicts/lists) of objects
