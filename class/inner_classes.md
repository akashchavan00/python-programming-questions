An inner class (also called a nested class) is simply a class defined
inside another class. The inner class is treated as an attribute of
the outer class. It is useful when a class only makes sense in the
context of another class, and you don't want it to exist on its own
in the rest of your code.

Example
Define a class inside another class:

    class Car:
        def __init__(self, brand, model):
            self.brand = brand
            self.model = model
            self.engine = self.Engine()

        class Engine:
            def __init__(self, horsepower=100):
                self.horsepower = horsepower

            def start(self):
                print(f"Engine started with {self.horsepower} HP")

    my_car = Car("Toyota", "Corolla")
    my_car.engine.start()

Here, `Engine` only makes sense as part of a `Car`. It groups related
code together and keeps the namespace clean, instead of having a
separate standalone `Engine` class floating around.

Accessing the inner class directly
You can also create an inner class object without going through the
outer class, by referencing it through the outer class name:

    engine = Car.Engine(250)
    engine.start()

Inner class with its own methods and the outer class
The inner class is independent of the outer class's instance data
unless you explicitly pass it in:

    class Student:
        def __init__(self, name):
            self.name = name
            self.address = self.Address("Unknown street", "Unknown city")

        def set_address(self, street, city):
            self.address = self.Address(street, city)

        class Address:
            def __init__(self, street, city):
                self.street = street
                self.city = city

            def show(self):
                print(f"{self.street}, {self.city}")

    s1 = Student("Tobias")
    s1.address.show()

    s1.set_address("Main Street", "Oslo")
    s1.address.show()

Why use inner classes?
- Groups small helper classes that are only relevant to one outer
  class, instead of cluttering the file with standalone classes.
- Keeps related code organized together, which can make large
  programs easier to read.
- Hides the inner class from being used freely elsewhere, encouraging
  it to only be used through the outer class.

Note: Inner classes are not used very often in everyday Python code.
Many Python developers prefer separate classes or composition instead,
since Python does not need inner classes for access control the way
Java does. But they are a valid tool when a class is a very small,
tightly coupled detail of another class.
