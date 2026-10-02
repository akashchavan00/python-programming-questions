All class have a built-in method called __init__(), which is always executed when the class is being initiated

The __init__() method is used to assign values to object properties, or to perform operations that are necessary when the object is being created.

Create a class named Person, use the __init__() method to assign values for name and age:

    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age

    p1 = Person("Emil", 36)

    print(p1.name)
    print(p1.age)

Note: The __init__() method is called automatically every time the class is being used to create a new object.

Without the __init__() method, you would need to set properties manually for each object:

You can also set default values for parameters in the __init__() method:

    class Person:
        def __init__(self, name, age=18):
            self.name = name
            self.age = age

    p1 = Person("Emil")
    p2 = Person("Tobias", 25)

    print(p1.name, p1.age)
    print(p2.name, p2.age)

The init method can have as many parameters as you need


Python Self Parameter:
The self paramter is a reference to the current instance of the class
It is used to access properties and methods that belong to that class.
The self paramter must be the first parameter of any method in the class.
Without self python would not know which object's properties you want to access.
It does not need to be named self you can call it whatever you like but it has to be the first parameter of any method in the class.
While you can use a different name, it is strongly recommended to use self as it is the convention in Python and makes your code more readable to others.
We can also call other methods within the class using self.
