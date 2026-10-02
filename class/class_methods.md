Methods are functions that belong to the class they define the beahavior
of objects from the class.

All methods must have the self as the first parameter.

Methods can access and modify object properties using self.

The __str__() method is a special method that controls what is returned 
when the object is printed

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name} ({self.age})"

p1 = Person("Tobias", 36)
print(p1)