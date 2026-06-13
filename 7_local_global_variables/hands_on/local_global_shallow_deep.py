# LOCAL AND GLOBAL VARIABLES

x = 10

def show():
    print(x)

show()

# Output
# 10

# Why
# Python first searches inside local scope
# if not found, it searches global scope


x = 10

def change():
    x = 20
    print(x)

change()
print(x)

# Output
# 20
# 10

# Why
# x inside function is a completely new local variable
# global x remains unchanged


x = 10

def change():
    global x
    x = 20

change()
print(x)

# Output
# 20

# Why
# global tells Python:
# "Use the variable from global scope"


count = 0

def increment():
    global count
    count += 1

increment()
increment()

print(count)

# Output
# 2


# Common Interview Question

x = 10

def test():
    print(x)
    x = 20

test()

# Error
# UnboundLocalError

# Why
# Python sees x = 20
# and immediately decides x is local

# So print(x) tries to access a local variable
# before it has been assigned


# LEGB Rule

# L -> Local
# E -> Enclosing
# G -> Global
# B -> Built-in

x = "global"

def outer():

    x = "enclosing"

    def inner():
        x = "local"
        print(x)

    inner()

outer()

# Output
# local

# Python searches:
# Local -> Enclosing -> Global -> Built-in


# Enclosing Scope

def outer():

    x = 10

    def inner():
        print(x)

    inner()

outer()

# Output
# 10

# inner() cannot find x locally
# so it checks enclosing scope


# nonlocal Keyword

def outer():

    x = 10

    def inner():
        nonlocal x
        x = 20

    inner()

    print(x)

outer()

# Output
# 20

# Why
# nonlocal modifies variable from enclosing scope
# not global scope


# SHALLOW COPY AND DEEP COPY

import copy


# Assignment

a = [1, 2, 3]
b = a

b[0] = 100

print(a)
print(b)

# Output
# [100, 2, 3]
# [100, 2, 3]

# Why
# Both variables point to same object


# Verify

a = [1, 2, 3]
b = a

print(id(a))
print(id(b))

# Same address


# SHALLOW COPY

a = [[1, 2], [3, 4]]

b = a.copy()

print(id(a))
print(id(b))

# Different addresses

# Outer list copied
# Inner lists NOT copied


a = [[1, 2], [3, 4]]

b = a.copy()

b[0][0] = 100

print(a)
print(b)

# Output
# [[100, 2], [3, 4]]
# [[100, 2], [3, 4]]

# Why
# Inner list is shared


# Visualization

# a ----> [ addr1 , addr2 ]
# b ----> [ addr1 , addr2 ]

# outer lists differ
# inner lists same


a = [[1, 2], [3, 4]]

b = a.copy()

b[0] = [100, 200]

print(a)
print(b)

# Output
# [[1, 2], [3, 4]]
# [[100, 200], [3, 4]]

# Why
# Replacing entire inner list changes only b


# DEEP COPY

import copy

a = [[1, 2], [3, 4]]

b = copy.deepcopy(a)

b[0][0] = 100

print(a)
print(b)

# Output
# [[1, 2], [3, 4]]
# [[100, 2], [3, 4]]

# Why
# Every nested object copied recursively


# Visualization

# a ----> [ addr1 , addr2 ]
#
# b ----> [ addr3 , addr4 ]

# Nothing shared


# Interview Question

a = [[0] * 3] * 3

print(a)

# Output
# [[0,0,0],[0,0,0],[0,0,0]]

# Looks fine...


a[0][0] = 1

print(a)

# Output
# [[1,0,0],
#  [1,0,0],
#  [1,0,0]]

# Why

# [0] * 3 creates

# addr1 -> [0,0,0]

# Then

# [addr1] * 3

# creates

# [
#   addr1,
#   addr1,
#   addr1
# ]

# All rows point to same list


# Verify

a = [[0] * 3] * 3

print(id(a[0]))
print(id(a[1]))
print(id(a[2]))

# All same


# Correct Way

a = [[0] * 3 for _ in range(3)]

print(id(a[0]))
print(id(a[1]))
print(id(a[2]))

# Different addresses


a[0][0] = 1

print(a)

# Output
# [[1,0,0],
#  [0,0,0],
#  [0,0,0]]

# Now every row is independent


# QUICK SUMMARY

# b = a
# No copy
# Same object

# b = a.copy()
# Shallow copy
# Outer copied
# Inner shared

# b = copy.deepcopy(a)
# Deep copy
# Everything copied

# global
# Modify global variable inside function

# nonlocal
# Modify enclosing variable inside nested function

# LEGB
# Local -> Enclosing -> Global -> Built-in