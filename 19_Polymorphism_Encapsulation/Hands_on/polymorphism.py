# Polymorphism
# By name ==> Poly => Many
            #   Morph => Forms
# So using polymorphism we can make same method work differently for different kind of objects


# Parent class (common interface)
class Person:
    def calculate_salary(self):
        pass


# Manager receives a fixed salary
class Manager(Person):
    def __init__(self, salary):
        self.salary = salary

    def calculate_salary(self):
        return self.salary


# Employee receives salary + bonus
class Employee(Person):
    def __init__(self, salary, bonus):
        self.salary = salary
        self.bonus = bonus

    def calculate_salary(self):
        return self.salary + self.bonus


# Intern receives a stipend
class Intern(Person):
    def __init__(self, stipend):
        self.stipend = stipend

    def calculate_salary(self):
        return self.stipend


obj = Manager(1000)
print(obj.calculate_salary())


# Now let's take reference of all three of these

staff = [
    Manager(100000),
    Employee(70000, 10000),
    Intern(15000)
]

# Same method call -> Different behavior depending on object type
for person in staff:
    print(person.calculate_salary())

# The loop does NOT care whether the object is:
# - Manager
# - Employee
# - Intern
#
# It only knows:
#     person.calculate_salary()
#
# Python decides at runtime which implementation to execute.
#
# This is called Runtime Polymorphism.



# Without polymorphism:

# if isinstance(person, Manager):
 
# elif isinstance(person, Employee):
 
# elif isinstance(person, Intern):


# With polymorphism:

# person.calculate_salary()

# No type checking required.



# In Python, inheritance is not mandatory for polymorphism.
# Python only checks whether the object has the required method.

class Contractor:
    def calculate_salary(self):
        return 50000


# Contractor is NOT a subclass of Person.
# Yet it works because it has calculate_salary().

people = [Manager(100000), Contractor()]

for p in people:
    print(p.calculate_salary())

# This is called Duck Typing:

# "If it walks like a duck and quacks like a duck,
# treat it as a duck."

# Python cares about behavior, not necessarily inheritance.

# Now We'll talk about

# Method Overriding
# Method Overloading 
# Operator Ove

# Method Overriding

# When a child class provides its own implementation of a method that already exists in the parent class.
# We've already seen this in Inheritance

class Employee:
    def work(self):
        print("Employee is working")


class Developer(Employee):
    def work(self):
        print("Developer is writing code")

dev = Developer()

dev.work()

# the child is overriding the parent's methods


# Method Overloading

# add(int a)
# add(int a, int b)
# add(int a, int b, int c)

# it's the classic example we already know if two methods have same name but different parameters they are going to 
# act differently

# BUUUUUTTTT python doesn't support it....

# python only keeps the last called method


class Employee:

    def calculate_salary(self, salary):
        return salary

    def calculate_salary(self, salary, bonus):
        return salary + bonus
    
emp = Employee()

print(emp.calculate_salary(50000))  # => will throw an error expecting bonus



# Operator Overloading

# changing the behaviour of operators for custom objects

print(10 + 20)

print("Hello" + "World")

# Here "+" is working differently for different objects# Now We'll talk about

# Method Overriding
# Method Overloading 
# Operator Ove

# Method Overriding

# When a child class provides its own implementation of a method that already exists in the parent class.
# We've already seen this in Inheritance

class Employee:
    def work(self):
        print("Employee is working")


class Developer(Employee):
    def work(self):
        print("Developer is writing code")

dev = Developer()

dev.work()

# the child is overriding the parent's methods


# Method Overloading

# add(int a)
# add(int a, int b)
# add(int a, int b, int c)

# it's the classic example we already know if two methods have same name but different parameters they are going to 
# act differently

# BUUUUUTTTT python doesn't support it....

# python only keeps the last called method


class Employee:

    def calculate_salary(self, salary):
        return salary

    def calculate_salary(self, salary, bonus):
        return salary + bonus
    
emp = Employee()

print(emp.calculate_salary(50000))  # => will throw an error expecting bonus



# Operator Overloading

# changing the behaviour of operators for custom objects

print(10 + 20)

print("Hello" + "World")

# Here "+" is working differently for different objects
