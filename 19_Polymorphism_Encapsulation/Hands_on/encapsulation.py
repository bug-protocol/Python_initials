# Encapsulation
class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

p1 = Person('Jordan', 'Jash')
p2 = Person('Steve', 'Harrington')

print(p1.first_name)
print(p2.first_name)

# Here first_name and last_name are acting as the instance_variable which is 
# a special type of variable which takes in different values depending upon
# the different type of objects.

# Encapsulation generally leads to bundling data and methods together with access controls like private, public mode specifics.

# Let's start with an example

# class BankAccount:
#     def __init__(self):
#         self.balance = 1000

# acc = BankAccount()

# acc.balance = -50000

# print(acc.balance)

# here anybody can access data and methods from a crucial class. which should not be possible

# Hence to stop this to happen we'll use access modifiers like we can private this stuff

# In python we use "__" to turn any variable or method to private

class BankAccount:
    def __init__(self):
        self.__balance = 1000
        self.name = "Rohan"

acc = BankAccount()

# acc.__balance = -50000

# print(acc.balance) => it'll throw an error because variable itself got changed


# but private doesn't mean truly hidden it can be accessed easily by following 
# print(acc.__balance)

# Here python performed name mangling like => __balance became _BankAccount__balance

# Hence nothing is truly private in python. 
# It's just people rely on significations that if an attribute has been set private it should not be messed with.


# Use of getter and setter functions to access and change values

class Account:
    def __init__(self):
        self.__balance = 10000

    # Getter Function
    def get_balance(self):
        return self.__balance
    

    # Setter Function
    def set_balance(self, data):
        self.__balance = data



acc = Account()
print(acc.get_balance())

acc.set_balance(2400)

print(acc.get_balance())

# Benefit of Getter and Setter Functions
# Earlier things were pretty straight forward to be changed.
# Now we're using functions hence 
# we can insert checks to enable valid changes

class Account:
    def __init__(self):
        self.__balance = 10000

    # Getter Function
    def get_balance(self):
        return self.__balance
    

    # Setter Function
    def set_balance(self, data):
        if type(data) == int:
            self.__balance = data
        else:
            print("Give a valid input")


acc = Account()
print(acc.get_balance())

acc.set_balance("Two zero one")

print(acc.get_balance())


# Public vs Protected vs Private Modes

class ModeSpecifiers:
    def __init__(self):
        self.name = "Public"
        self._salary = "Protected"
        self.__password = "Private"

obj = ModeSpecifiers()

print(obj.name)       # Works  

print(obj._salary)    # Works but the convention of single underscore means you shouldn't directly access this variable

print(obj.__password) # Error