# Q7: Bank Account System with Custom Exceptions

## Question
Build a small banking simulation:
1. Define custom exceptions `InvalidAmountError` and `InsufficientFundsError` (both subclassing `Exception`).
2. Implement a `BankAccount` class with `deposit(amount)`, `withdraw(amount)`, and a `transfer(other_account, amount)` method.
   - `deposit`/`withdraw` should raise `InvalidAmountError` for zero/negative amounts.
   - `withdraw`/`transfer` should raise `InsufficientFundsError` if the balance is too low.
3. Keep a transaction history log inside each account (a list of strings).
4. Write driver code that attempts several valid and invalid operations, using `try/except/else/finally` to handle each case gracefully and print appropriate messages without crashing the program.

## Approach
1. Custom exceptions are created by subclassing `Exception`, which lets calling code catch specific error types instead of generic ones — this is better error-handling design than checking error message strings.
2. Validate inputs at the top of each method and `raise` the appropriate custom exception with a descriptive message.
3. `transfer` is implemented by composing `withdraw` (on `self`) and `deposit` (on the other account) — if `withdraw` raises, `deposit` never runs, keeping the operation atomic-ish for this simple example.
4. In the driver code, `try/except SpecificError as e: ... else: ... finally: ...` demonstrates the full exception-handling flow: `else` runs only if no exception occurred in the `try` block, and `finally` always runs regardless (e.g., for logging "operation attempted").

## Concepts Used
- Custom exception classes (`class InvalidAmountError(Exception)`)
- Raising exceptions with `raise ExceptionType("message")`
- `try/except/else/finally` (the complete exception-handling structure)
- Catching multiple, specific exception types
- OOP: classes, instance methods, state (balance, history)
- Lists of strings as a simple audit log
