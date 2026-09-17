"""
Q10: JSON-based Contact Book (CRUD)
Persists contacts to a JSON file, demonstrating file I/O + the json module.
"""

import json
import os


class ContactNotFoundError(Exception):
    """Raised when trying to update/delete/search a contact that doesn't exist."""


class ContactBook:
    def __init__(self, filepath="contacts.json"):
        self.filepath = filepath
        self._contacts = self._load()

    def _load(self):
        if not os.path.exists(self.filepath):
            return {}
        try:
            with open(self.filepath, "r") as f:
                return json.load(f)
        except json.JSONDecodeError:
            # Empty or corrupted file -> start fresh instead of crashing.
            return {}

    def _save(self):
        with open(self.filepath, "w") as f:
            json.dump(self._contacts, f, indent=2)

    def add_contact(self, name, phone, email):
        self._contacts[name] = {"phone": phone, "email": email}
        self._save()

    def update_contact(self, name, **fields):
        if name not in self._contacts:
            raise ContactNotFoundError(f"No contact named {name!r}")
        self._contacts[name].update(fields)
        self._save()

    def delete_contact(self, name):
        if name not in self._contacts:
            raise ContactNotFoundError(f"No contact named {name!r}")
        del self._contacts[name]
        self._save()

    def search_contact(self, name):
        return self._contacts.get(name)

    def list_contacts(self):
        return dict(self._contacts)


def main():
    filepath = "contacts_demo.json"
    if os.path.exists(filepath):
        os.remove(filepath)  # start clean for a repeatable demo

    book = ContactBook(filepath)

    book.add_contact("Alice", "111-222-3333", "alice@example.com")
    book.add_contact("Bob", "444-555-6666", "bob@example.com")

    print("All contacts:")
    for name, info in book.list_contacts().items():
        print(f"  {name}: {info}")

    book.update_contact("Alice", phone="999-999-9999")
    print("\nAfter updating Alice's phone:")
    print(" ", book.search_contact("Alice"))

    try:
        book.update_contact("Charlie", phone="000-000-0000")
    except ContactNotFoundError as e:
        print(f"\nExpected error: {e}")

    book.delete_contact("Bob")
    print("\nAfter deleting Bob:")
    for name, info in book.list_contacts().items():
        print(f"  {name}: {info}")

    # Simulate reopening the app: create a new ContactBook instance
    # pointing at the same file to prove data persisted.
    reopened = ContactBook(filepath)
    print("\nReopened contact book (loaded from disk):")
    for name, info in reopened.list_contacts().items():
        print(f"  {name}: {info}")


if __name__ == "__main__":
    main()
