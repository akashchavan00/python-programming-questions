Inheritance lets you create a new class that reuses, extends, or
modifies the behavior of another class. The new class is called the
child class (or derived/subclass), and the class it inherits from is
called the parent class (or base/superclass).

This avoids writing the same code again and again. You put the common
logic in the parent class, and each child class only adds or changes
what is different.

Example
Create a parent class Person:

    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age

        def introduce(self):
            print(f"My name is {self.name} and I am {self.age} years old")

Create a child class Student that inherits from Person:

    class Student(Person):
        pass

    s1 = Student("Tobias", 20)
    s1.introduce()

The Student class has no content of its own, but because it inherits
from Person, it has access to Person's properties and methods.

Add the __init__() method to the child class
When you add __init__() in the child class, it will no longer
automatically call the parent's __init__(). You use `super()` to call
the parent class's methods.

    class Student(Person):
        def __init__(self, name, age, school):
            super().__init__(name, age)
            self.school = school

        def introduce(self):
            super().introduce()
            print(f"I study at {self.school}")

    s1 = Student("Tobias", 20, "MIT")
    s1.introduce()

`super()` lets you call methods from the parent class, so you don't
have to repeat the parent's logic.

Overriding methods
A child class can completely replace (override) a method from the
parent class by defining a method with the same name:

    class Animal:
        def sound(self):
            print("Some generic animal sound")

    class Dog(Animal):
        def sound(self):
            print("Bark")

    class Cat(Animal):
        def sound(self):
            print("Meow")

    a = Animal()
    d = Dog()
    c = Cat()

    a.sound()
    d.sound()
    c.sound()

Multiple inheritance
A class can inherit from more than one parent class:

    class Father:
        def skills(self):
            print("Can drive, can cook")

    class Mother:
        def talents(self):
            print("Can paint, can sing")

    class Child(Father, Mother):
        pass

    c = Child()
    c.skills()
    c.talents()

Multilevel inheritance
A class can inherit from a class that itself inherits from another
class:

    class Animal:
        def eat(self):
            print("This animal eats food")

    class Mammal(Animal):
        def walk(self):
            print("This mammal can walk")

    class Dog(Mammal):
        def bark(self):
            print("Woof")

    d = Dog()
    d.eat()
    d.walk()
    d.bark()

Why use inheritance?
- Avoids duplicating code across similar classes.
- Lets you build specialized classes on top of general ones.
- Makes code easier to extend, you add new child classes without
  touching the parent class.
