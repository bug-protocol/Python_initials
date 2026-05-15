# How we store string in Python??

# using quotes

# single quote

from decimal import Decimal
name = 'Ashu'
print(name)

# double quote

name2 = "Steve"
print(name2)

# triple quotes

message = '''Hello
Welcome to Python
Programming'''
print(message)


# strings are ordered and immutable

# name[0] = 'H'
# it'll give an error

# Accessing characters in a string

word = "Python"

print(word[0])   
print(word[2])   


# Python stores strings as:

  # objects of class str
  # sequence of unicode characters

  # Creates a str object in memory

#   Stores characters:

# Stores metadata like:
    # length of string
    # encoding type
    # hash value (sometimes cached)
    # reference count

# Python3 stores string as unicode


# Q: 2 :---> Explore NONE==NONE

# None is a special built-in constant in Python that represents:

    # absence of value
    # null value
    # nothing

print(type(None))

print(None==None)

# here both operands share the same object hence it returns true!!

# boolean value of none

print(bool(None))


# it behaves as a falsy value in conditions

# DOCSTRINGS

def multiply(a, b):
    """Returns multiplication of two numbers."""
    
    return a * b

help(multiply)

# used for documenting, for defining the work of a module as function or class or anything



# Float vs Decimal

print(0.1 + 0.2)

# float uses binary floating-point representation internally.

# it'll give 0.30000000000000004 ===> Because computers store floats in binary, and many decimal values cannot be represented exactly in binary.


# Python provides the Decimal type from the decimal module.

# It stores decimal numbers more accurately.


x = Decimal('0.1')
y = Decimal('0.2')

print(x + y)

# Because Decimal stores numbers in:

# decimal format
# not binary approximation


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
