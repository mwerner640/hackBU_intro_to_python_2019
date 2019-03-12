# Advanced Python Tutorial (Classes)
# Author: Melanie Chen
# Based on material from https://docs.python.org/3/tutorial/classes.html

line = "________________________________________________________"

# Classes bundle data and functionality together
# Creating a new class creates a new TYPE of object, allowing new INSTANCES of that type to be made
# Each class instance can have attributes attached to it for maintaining its state
# Each class instance can have methods attached to it for modifying state

# Multiple names (in multiple scopes) can be bound to the same object. This is often known as aliasing. 
# Since aliases behave like pointers in some respects, passing objects is cheap.
# This also means that if a function modifies an object passed as an argument, the caller will see the change.

class Room:
    def __init__(self, color, windows, doors):
        self.color = color
        self.windows = windows
        self.doors = doors

def paintRoom(room, color):
    room.color = color

my_room = Room("purple", 2, 1)
print(my_room.color)
paintRoom(my_room, "green")
print(my_room.color)

print(line)

# A NAMESPACE is a mapping from names to objects. Examples include: the set of built-in names (like abs()), global names in a module, and local names in a function invocation. There is no relation between names in different namespaces.
# A module is an object.

import example1
import example2

print(example1.maximize([5,6,2,7]))
print(example2.maximize([5,6,2,7]))

print(line)

# An ATTRIBUTE is any name following a dot. For example, in the expression z.real, real is an attribute of the object z.
# Attributes can be read-only or writable.
# Writable attributes can be modified or deleted.

example1.hello = "Hello, World!"
print(example1.hello)
del example1.hello
try:
    print(example1.hello)
except AttributeError as e:
    print(e)

print(line)

# A SCOPE is a textual region of a Python program where a namespace is directly accessible. "Directly accessible" means an unqualified reference to the name attempts to find the name in the namespace.
# example1.maximize is the full qualified name. maximize is the unqualified name.
# Search in the order: innermost scope (local names) -> scopes of enclosing functions (non-local, but non-global names) -> next-to-last scope (current module's global names) -> outermost scope (built-in names)

def my_enclosing():
    def my_fun():
        # Local x
        x = 4
        print(x)
    
    x = 5
    print(x)
    my_fun()
    print(x)

my_enclosing()

print(line)

# We need to define a class before we can use it. The below syntax describes the most basic class definition.

class MyClass:
    # Data and methods go here
    pass

# When a class definition is entered, a new namespace is created and used as the local scope.
# When a class definition is exited, a CLASS OBJECT is created. We return to the original scope and the class object is now bound to the class name (e.g. MyClass).
# We can do two things with this class object, attribute references and instantiation.

# Attribute references use the same syntax used for all attribute references in Python.

class SimpleExample:
    '''This is a docstring'''
    my_data = 42

    def get_my_data(self):
        return my_data

print(SimpleExample.my_data)
print(SimpleExample.get_my_data)

print(line)

# Class instantiation uses function notation. Pretend the class object is a parameterless function that returns a new INSTANCE of the class.
# The class object is like the blueprint. The class instance is like the actual house.

my_simple_example = SimpleExample()

# Let's keep going with the blueprint-house analogy. What if we want all the houses to share some common features?
# When a class defines the __init__() method, class instantiation automatically invokes __init__().

class House:
    street = "Leroy Avenue"

    def __init__(self, color, rooms):
        self.color = color
        self.rooms = rooms
        self.levels = 2

# Every house starts out with two levels, plus the color and number of rooms that a homeowner chooses. These instance variables contain the state.
# Say the homeowner later renovates and adds another room.
    
    def setNumRooms(self, numRooms):
        self.rooms = numRooms

# This class method modifies the state.
# It is common for programmers to define getters and setters for their instance variables.
    
    def getNumRooms(self):
        return self.rooms

    def setColor(self, color):
        self.color = color

    def getColor(self):
        return self.color

    def setLevels(self, levels):
        self.levels = levels

    def getLevels(self):
        return self.levels

# What can we do with instance objects? We can reference their attributes (data attributes and methods)!

# First, let's initialize the class instance using the __init__() method (called a constructor in some languages).

my_house = House("gray", 4)

# Now, let's reference a data attribute.

print(my_house.rooms)

# Or, let's reference a method.

print(my_house.getColor())

print(line)

# What is the difference between House.getColor() and my_house.getColor()? 
# Technically House.getColor() is a function object and my_house.getColor() is a method object.
# But, an easier way to think about it is that my_house.getColor() is equivalent to MyHouse.getColor(my_house).
# Basically, "self" refers to that particular instance object.

# Let's see an example.
class Dog:
    kind = "canine"

    def __init__(self, name):
        self.name = name

d = Dog("Fido")
e = Dog("Buddy")

print(Dog.kind)
print(Dog.__init__)
print(d.kind)
print(d.name)
print(e.kind)
print(e.name)

print(line)

# In this example, the kind variable is a class variable. Its state is shared by all instances of the Dog class. The name variable is an instance variable. It is tied to one particular instance.

# What's wrong with this example?
class Dog:
    tricks = []

    def __init__(self, name):
        self.name = name

    def add_trick(self, trick):
        self.tricks.append(trick)

d = Dog('Fido')
e = Dog('Buddy')
d.add_trick('roll over')
e.add_trick('play dead')
print(d.tricks)

print(line)

# The tricks variable is a class variable, which means every instance of Dog shares its state. This is like a static variable in Java. If Fido learns a new trick, Buddy should not also gain this skill! This variable is better suited as an instance variable.

# More on self: The first argument of a method is conventionally called self, but there is nothing special about this word. We could use "me" instead, for example. 

# We already know how to reference data attributes and methods from outside the class, but what about within it?
class Dog:
    def __init__(self, name):
        self.name = name
        self.tricks = []

    def add_trick(self, trick):
        self.tricks.append(trick)

    def add_many_tricks(self, listOfTricks):
        for trick in listOfTricks:
            self.add_trick(trick)

