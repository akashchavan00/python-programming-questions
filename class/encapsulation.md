Encapsulation means wrapping data (properties) and the methods that
work on that data inside a single unit, the class, and restricting
direct access to some of the object's components.

In simple words: you hide the internal details of an object and only
allow access through methods you provide. This protects the data from
being changed accidentally or incorrectly from outside the class.

Python does not have real "private" keywords like Java or C++, but it
uses naming conventions to indicate access levels:

- public member: normal name, e.g. `self.name`. Accessible from
  anywhere.
- protected member: single underscore prefix, e.g. `self._name`. By
  convention it should only be used inside the class or subclasses,
  but Python does not actually block access.
- private member: double underscore prefix, e.g. `self.__name`. Python
  renames it internally (name mangling) so it becomes harder to access
  from outside the class.

Example
Public property, accessible from anywhere:

    class Person:
        def __init__(self, name):
            self.name = name

    p1 = Person("Tobias")
    print(p1.name)
    p1.name = "Linus"
    print(p1.name)

Example
Private property, using double underscore:

    class Person:
        def __init__(self, name, balance):
            self.name = name
            self.__balance = balance

        def get_balance(self):
            return self.__balance

        def deposit(self, amount):
            if amount > 0:
                self.__balance += amount

    p1 = Person("Tobias", 1000)
    print(p1.get_balance())

    p1.deposit(500)
    print(p1.get_balance())

    # print(p1.__balance)
    # AttributeError: 'Person' object has no attribute '__balance'

Even though `__balance` is "private", you can technically still
access it using Python's name mangling trick:

    print(p1._Person__balance)

This proves Python does not have true private variables, it just
makes it inconvenient to access them directly, trusting the developer
to respect the convention.

Getters and Setters
A common pattern in encapsulation is using getter and setter methods
to read and update a private property, instead of accessing it
directly. This lets you add validation logic.

    class Person:
        def __init__(self, age):
            self.__age = age

        def get_age(self):
            return self.__age

        def set_age(self, age):
            if age < 0:
                print("Age cannot be negative")
            else:
                self.__age = age

    p1 = Person(25)
    p1.set_age(-5)
    print(p1.get_age())

Python also supports a cleaner way to write getters and setters using
the `@property` decorator:

    class Person:
        def __init__(self, age):
            self.__age = age

        @property
        def age(self):
            return self.__age

        @age.setter
        def age(self, value):
            if value < 0:
                print("Age cannot be negative")
            else:
                self.__age = value

    p1 = Person(25)
    p1.age = -5
    print(p1.age)
    p1.age = 30
    print(p1.age)

Why use encapsulation?
- Protects data from being modified in unexpected ways.
- Lets you add validation before changing a value.
- Hides internal implementation, so you can change it later without
  breaking code that uses the class.
