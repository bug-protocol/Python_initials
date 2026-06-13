#common built in python functions
# Type Conversion

int("10")        # 10
float("3.14")    # 3.14
str(100)         # "100"
list("abc")      # ['a', 'b', 'c']
tuple([1, 2])    # (1, 2)
set([1, 1, 2])   # {1, 2}
dict()
bool(1)             # True

# Maths
abs(-5)          # 5
round(3.14159, 2) # 3.14
pow(2, 3)        # 8 => 2 ^ 3
min(1, 2, 3)     # 1
max(1, 2, 3)     # 3
sum([1, 2, 3])   # 6
divmod(10, 3)    # (3, 1) => returns both quotient and reminder in a tuple

# Iterables
len([1, 2, 3])       # 3
sorted([3, 1, 2])    # [1, 2, 3]
rv = list(reversed([1, 2, 3]))
print(rv)
print(list(enumerate(['a', 'b'])))  # => when needed both index and value while iterating
print(list(zip([1, 2, 3], ['a', 'b', 'c'])))    # => combines elements from multiple iterables position-wise
print(list(map(str, [1, 2, 3])))    # => applies a function to every element of an iterable
print(list(filter(lambda x: x > 0, [-1, 2, 3])))  # => keeps the elements for which condition is True
any([False, (), True])   # True => if atleast one element is truthy else False
all([True, True])    # True => only if all elements are true...if anyone is falsy it returns false

# Character/ Unicode
ord('A')     # 65
chr(65)      # 'A'

# Object information
type(10)           # <class 'int'>
id("hello")        # memory identity
isinstance(10, int) # True => checks whether a particular object belongs to a particular type of class or type

# Input/Output
print("Hello")
name = input("Enter name: ")

# Variable Scope
# globals()
# locals()

# callable(greet) # checks whether an object can be called using ()
# like suppose greet() function is callable => Hence true
# else => false

range(5) # => 0, 1, 2, 3, 4

help(len) # => used to check the documentation of a particular method or function
dir(len) # => methods associated with that particular object 