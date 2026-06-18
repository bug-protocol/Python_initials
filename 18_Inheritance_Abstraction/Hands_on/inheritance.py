# Inheritance :- 
# It allows one class (child class) to inherit properties and methods from another class(parent class)

# Basic Syntax
class A:
    def func1(self):
        print("Func1 is running")

class B(A):
    pass

call = B()
call.func1()
# python internally converts this to A.func1(call)
# so if no self is passed the parent class A would still expect an argument
# which will lead to an error

# Parent Constructor Inheritance

class Parent:
    def __init__(self):
        print("We're trying out something!")

class Child(Parent):
    pass

obj1 = Child()

# child has no constructor hence it uses parent's constructor

# Child can override parent's methods

class Parent1:
    def func(self):
        print("We're trying out something!")

class Child1(Parent1):
    def func(self):
        print("Looking at this overriding!")

obj2 = Child1()
obj2.func()

# use of super()

class Parent2:
    def func(self):
        print("We're here checking out super() method!")

class Child2(Parent2):
    def func1(self):
        super().func()
        print("Let's see if it works!")

obj3 = Child2()
obj3.func1()


# using super() with Constructor

class Parent3:
    def __init__(self, name):
        self.name = name

class Child3(Parent3):
    def __init__(self, name, course):
        super().__init__(name)
        self.course = course

obj4 = Child3("Ashu", "Python")
print(obj4.name)
print(obj4.course)

# Types of Inheritance 

# Single Inheritance

class Parent3:
    pass

class Child3(Parent3):
    pass

# Multilevel Inheritance

class Parent:
    pass
class Child1(Parent):
    pass
class Child2(Child1):
    pass

# Multiple Inheritance

class Parent1:
    pass
class Parent2:
    pass
class Child(Parent1, Parent2):
    pass

# Hierarchial Inheritance

# one parent -> many children

class Parent:
    pass
class Child1(Parent):
    pass
class Child2(Parent):
    pass

# Hybrid Inheritance

class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass

# isinstance()
# checks object type
class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        print("B")

class C(A):
    def show(self):
        print("C")

class D(B, C):
    pass

d = D()
d.show()

# Output
# True
# True

# issubclass()
# check class relationship

class Employee:
    def __init__(self, name):
        self.name = name
        print("Employee Constructor")

    def work(self):
        print(f"{self.name} is working")

    def get_role(self):
        print("General Employee")


class Developer(Employee):
    def __init__(self, name, language):
        super().__init__(name)
        self.language = language
        print("Developer Constructor")

    def work(self):
        print(f"{self.name} writes {self.language} code")
        super().work()

    def get_role(self):
        print("Developer")
        super().get_role()


class Manager(Employee):
    def __init__(self, name):
        super().__init__(name)
        print("Manager Constructor")

    def work(self):
        print(f"{self.name} manages the team")
        super().work()

    def get_role(self):
        print("Manager")
        super().get_role()


class TechLead(Developer, Manager):
    def __init__(self, name, language):
        super().__init__(name, language)
        print("TechLead Constructor")

    def get_role(self):
        print("Tech Lead")
        super().get_role() 



