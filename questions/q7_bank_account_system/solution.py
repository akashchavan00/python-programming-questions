"""
Q7: Bank Account System with Custom Exceptions
Demonstrates custom exceptions and the full try/except/else/finally flow.
"""


class InvalidAmountError(Exception):
    """Raised when an amount is zero, negative, or otherwise invalid."""


class InsufficientFundsError(Exception):
    """Raised when a withdrawal/transfer exceeds the available balance."""


class BankAccount:
    def __init__(self, owner, balance=0.0):
        self.owner = owner
        self.balance = balance
        self.history = []

    def deposit(self, amount):
        if amount <= 0:
            raise InvalidAmountError(f"Deposit amount must be positive, got {amount}")
        self.balance += amount
        self.history.append(f"Deposited {amount:.2f}, new balance {self.balance:.2f}")

    def withdraw(self, amount):
        if amount <= 0:
            raise InvalidAmountError(f"Withdrawal amount must be positive, got {amount}")
        if amount > self.balance:
            raise InsufficientFundsError(
                f"Cannot withdraw {amount:.2f}; balance is only {self.balance:.2f}"
            )
        self.balance -= amount
        self.history.append(f"Withdrew {amount:.2f}, new balance {self.balance:.2f}")

    def transfer(self, other, amount):
        # withdraw() raises before deposit() runs if funds are insufficient,
        # so the transfer never "partially" happens.
        self.withdraw(amount)
        other.deposit(amount)
        self.history.append(f"Transferred {amount:.2f} to {other.owner}")

    def __str__(self):
        return f"{self.owner}'s account: balance={self.balance:.2f}"


def attempt(description, action):
    """Run `action` and report the result using try/except/else/finally."""
    print(f"\n> {description}")
    try:
        action()
    except InvalidAmountError as e:
        print(f"  Rejected (invalid amount): {e}")
    except InsufficientFundsError as e:
        print(f"  Rejected (insufficient funds): {e}")
    else:
        print("  Success.")
    finally:
        print("  (operation attempted)")


def main():
    alice = BankAccount("Alice", balance=100.0)
    bob = BankAccount("Bob", balance=20.0)

    attempt("Alice deposits 50", lambda: alice.deposit(50))
    attempt("Alice withdraws -10 (invalid)", lambda: alice.withdraw(-10))
    attempt("Bob withdraws 1000 (insufficient funds)", lambda: bob.withdraw(1000))
    attempt("Alice transfers 75 to Bob", lambda: alice.transfer(bob, 75))
    attempt("Bob transfers 500 to Alice (insufficient funds)", lambda: bob.transfer(alice, 500))

    print("\nFinal balances:")
    print(" ", alice)
    print(" ", bob)

    print("\nAlice's transaction history:")
    for entry in alice.history:
        print("  -", entry)


if __name__ == "__main__":
    main()
