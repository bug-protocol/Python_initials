# integer Data types ---> int , float , complex 

import random
age = 21
print(age)
print(type(age))


# float
price = 99.99
print(price)
print(type(price))

# complex 
iot = 1j
print(iot)
print(type(iot))


# Type conversion ==> 
tc = float(age)
print(type(tc))


# Random Number
print(random.randrange(1, 10))

# string
name = "Steve"
print(name)
print(type(name))

# Like many other popular programming languages, strings in Python are arrays of unicode characters.

# However, Python does not have a character data type, a single character is simply a string with a length of 1.

# Length of string
print(len(name))

# boolean
x = True
print(x)
print(type(x))


# list
arr = [1, 2, 3, 4]
print(arr)
print(type(arr))


# tuple
cord = (10, 20)
print(cord)
print(type(cord))


# set
num = {1, 2, 3, 4}
print(num)
print(type(num))


# Dictionary
student = {
    "name": "Steve",
    "age": 21
}
print(student)
print(type(student))


# None Type
data = None
print(data)
print(type(data))