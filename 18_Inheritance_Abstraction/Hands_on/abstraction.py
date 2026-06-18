# Abstraction
# Abstraction basically means hiding the implementation and showing the necessary details

# We've two instances that we should know for creating an abstract class in python.

# ABC => Abstract Base Class
# abstractmethod => method that must be implemented by children

from abc import ABC, abstractmethod
class MedApp(ABC):
    def db(self):
        print("Connected to Database!")

    @abstractmethod
    def security(self):
        print("Secure Authentication")

class accessDB(MedApp):
    def check(self):
        print("Check if it's running!")
    
    def security(self):
        print("We need the secure method from the head APP to begin with")

obj = accessDB()

obj.check()
obj.security()
obj.db()


# Abstract class => contains atleast one abstract method
# we can not make an object of the abstract class