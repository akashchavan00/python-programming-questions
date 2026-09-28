class myclass:
    x = 5

p1 = myclass()
print(p1.x)

del p1

# print(p1.x)  # This will raise an error because p1 has been deleted

# We can create a multiple objects from the same class
# Each object will have its own copy of the class attributes and methods

# Class definitions cannot be empty but if you for some reason have a class
# definition with no content put in the pass statement to avoid getting an error.

class person:
    pass

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print("Hello, my name is " + self.name + " and I am " + str(self.age) + " years old.")


p1 = Person("John", 36)

p1.greet()  # Output: Hello, my name is John and I am 36 years old.