class newClass:
    x = 5
    y = 10
obj1 = newClass()
print(obj1.x)
obj2 = newClass()
print(obj2.y)
# Deleting an object
del obj1



# Pass statement
class passClass:
    pass
obj3 = passClass()

# __init__ method => could be used to assign values to certain attributes of objects

class initClass:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = initClass("Steve", 23)
print(p1.name)
print(p1.age)

# Without use of init

class WinitClass:
    pass

p1 = WinitClass()
p1.name = "Romy"
p1.age = 24

print(p1.name)
print(p1.age)

# Default values could b