Abstraction means hiding the complex implementation details and only
showing the necessary features of an object. The user interacts with
a simple interface without needing to know how it works internally.

Think of a car. You just use the steering wheel, pedals, and gear to
drive it. You don't need to know how the engine, fuel injection, or
brakes work internally. That is abstraction in real life.

In Python, abstraction is usually achieved using abstract classes and
abstract methods, with help of the built-in `abc` module (Abstract
Base Class).

An abstract class is a class that cannot be used to create objects
directly. It only acts as a blueprint for other classes. An abstract
method is a method declared in the abstract class but has no
implementation, child classes must provide their own implementation.

Example
Create an abstract class Shape with an abstract method area():

    from abc import ABC, abstractmethod

    class Shape(ABC):
        @abstractmethod
        def area(self):
            pass

    class Circle(Shape):
        def __init__(self, radius):
            self.radius = radius

        def area(self):
            return 3.14 * self.radius * self.radius

    class Rectangle(Shape):
        def __init__(self, width, height):
            self.width = width
            self.height = height

        def area(self):
            return self.width * self.height

    c = Circle(5)
    r = Rectangle(4, 6)

    print(c.area())
    print(r.area())

Note: You cannot create an object directly from Shape because it is
abstract.

    shape = Shape()
    # TypeError: Can't instantiate abstract class Shape with abstract method area

Why use abstraction?
- It hides unnecessary details from the user.
- It forces child classes to implement required methods, so you don't
  forget to define important behavior.
- It makes code easier to maintain, since the user only cares about
  what a method does, not how it does it.

Abstraction vs Encapsulation
Abstraction is about hiding complexity by showing only the relevant
details (what an object does). Encapsulation is about hiding data by
restricting direct access to it (how the data is protected). They are
related but not the same thing.
