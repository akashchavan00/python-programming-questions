Properties are variables that belong to a class they store data for each 
object created from the class.

Class Properties vs Object Properties

Properties defined inside __init__() belong to each object (instance 
properties).

Properties defined outside methods belong to the class itself (class 
properties) and are shared by all objects

When you modify a class property, it affects all objects

Add New Properties
You can add new properties to existing objects:

Example
Add a new property to an object:

class Person:
  def __init__(self, name):
    self.name = name

p1 = Person("Tobias")

p1.age = 25
p1.city = "Oslo"

print(p1.name)
print(p1.age)
print(p1.city)

Note: Adding properties this way only adds them to that specific object, 
not to all objects of the class.

