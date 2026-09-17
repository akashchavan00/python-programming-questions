# Q10: JSON-based Contact Book (CRUD)

## Question
Build a simple contact book that persists data to a JSON file on disk. Implement:
- `add_contact(name, phone, email)`
- `update_contact(name, **fields)` — update one or more fields of an existing contact.
- `delete_contact(name)`
- `search_contact(name)` — return the contact dict or `None`.
- `list_contacts()` — return all contacts.

All operations should read from and write to a JSON file (e.g., `contacts.json`), so data survives between program runs. Handle the case where the file doesn't exist yet (start with an empty contact book) and handle invalid operations (e.g., updating/deleting a contact that doesn't exist) gracefully with clear messages instead of crashing.

## Approach
1. Represent the contact book internally as a dictionary keyed by name for O(1) lookups, updates, and deletes.
2. Write helper logic (`_load` / `_save`) that wraps `json.load` / `json.dump`. `_load` handles a missing file (`os.path.exists` check) and a corrupt/empty file (`json.JSONDecodeError`) by returning an empty dict instead of crashing.
3. Wrap the dictionary operations in a `ContactBook` class whose constructor loads existing data and whose mutating methods (`add`/`update`/`delete`) each save back to disk immediately, so the JSON file is always the source of truth.
4. Use `**fields` (keyword arguments) in `update_contact` so callers can update just the fields they want (e.g. `update_contact("Alice", phone="12345")`) without needing to pass every field.
5. Raise a custom `ContactNotFoundError` when a contact isn't found for update/delete, and catch it in the driver code to show graceful error handling.

## Concepts Used
- File I/O (`open`, reading/writing text files)
- The `json` module (`json.load`, `json.dump`, `json.JSONDecodeError`)
- Exception handling for missing/corrupt files (`FileNotFoundError` equivalent via `os.path.exists`)
- Dictionaries as the core data structure (keyed storage)
- Variable keyword arguments (`**kwargs`) for flexible partial updates
- OOP: encapsulating file-backed state inside a class
- Custom exceptions for domain-specific error handling
