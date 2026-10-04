Polymorphism means "many forms". In programming, it means that
different classes can have methods with the same name, but each class
can implement that method in its own way. You can then call the same
method on different objects and get different behavior depending on
the object's actual class.

Example
Different classes with the same method name:

    class Dog:
        def sound(self):
            print("Bark")

    class Cat:
        def sound(self):
            print("Meow")

    class Cow:
        def sound(self):
            print("Moo")

    animals = [Dog(), Cat(), Cow()]

    for animal in animals:
        animal.sound()

Even though `sound()` is called the same way on every object, each
one prints something different. Python does not care what type the
object actually is, it just calls `sound()` and lets the object decide
what to do. This is called duck typing: "If it walks like a duck and
quacks like a duck, it must be a duck."

Polymorphism with inheritance
This is the most common form of polymorphism. A parent class defines
a method, and each child class overrides it with its own version:

    class Shape:
        def area(self):
            return 0

    class Circle(Shape):
        def __init__(self, radius):
            self.radius = radius

        def area(self):
            return 3.14 * self.radius * self.radius

    class Square(Shape):
        def __init__(self, side):
            self.side = side

        def area(self):
            return self.side * self.side

    shapes = [Circle(5), Square(4)]

    for shape in shapes:
        print(shape.area())

Polymorphism with functions
You can write a function that works with any object, as long as that
object has the expected method, regardless of its class:

    class Car:
        def move(self):
            print("Drive on the road")

    class Boat:
        def move(self):
            print("Sail on the water")

    class Plane:
        def move(self):
            print("Fly in the sky")

    def start_moving(vehicle):
        vehicle.move()

    start_moving(Car())
    start_moving(Boat())
    start_moving(Plane())

The `start_moving()` function does not know or care what kind of
vehicle it receives, it just calls `move()` on it. That is
polymorphism in action.

Built-in polymorphism example
Python's own built-in functions are polymorphic too. For example,
`len()` works differently depending on the type of object:

    print(len("Hello"))      # counts characters in a string
    print(len([1, 2, 3]))    # counts items in a list
    print(len({"a": 1, "b": 2}))  # counts keys in a dictionary

Why use polymorphism?
- Lets you write generic code that works with many different object
  types.
- Makes it easy to add new classes later, as long as they implement
  the expected methods, existing code keeps working.
- Reduces the need for if/else chains that check an object's type
  before deciding what to do.
