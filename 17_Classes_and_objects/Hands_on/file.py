# Code is structured using classes and objects
# Features of OOP!
    # provides clear structure
    # makes code easier to maintain, reuse and debug
    # Helps in keeping the code DRY (Don't Repeat Yourself!)

# Classes and Objects

# Classes => defines how the object should look like
# Object => created based on classes

# Ex
# Fruits   =======>  Apple, Orange, Mango
# Classes  =======>  Objects

# When an object is created based on the class it inherits variables and functions defined inside the class.
# Class is blueprint of creating objects.

# Creating a class:-

class Test:
    x = 4
    y = 5

# Now Object

obj = Test()
print(obj.x)

obj2 = Test()
print(obj2.y)

# Deleting object

del obj2
# using just this the obj2 will be deleted

# The pass statement

class Person:
    pass
# can be used when we've no idea what to put inside that particular class

class 