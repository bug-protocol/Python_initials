# Decorators
# Decorators in Python are used to add extra functionality
# to an existing function without modifying its code.

# A decorator takes a function as input,
# wraps it with additional behavior,
# and returns a new function.

def decorator(func):

    def wrapper():
        print("Before Function")

        func()

        print("After Function")

    return wrapper


def greet():
    print("Hello")


greet = decorator(greet)

greet()

# # Output:
# # Before Function
# # Hello
# # After Function

# # The @ syntax is just a shortcut.

def decorator(func):

    def wrapper():
        print("Before Function")

        func()

        print("After Function")

    return wrapper


@decorator
def greet():
    print("Hello")


greet()

# Equivalent to:
#
# def greet():
#     print("Hello")
#
# greet = decorator(greet)

# Decorators can work with functions having arguments.

def decorator(func):

    def wrapper(name):
        print("Before Function")

        func(name)

        print("After Function")

    return wrapper


# @decorator
# def greet(name):
#     print(f"Hello {name}")


# greet("Ashutosh")

# # Output:
# # Before Function
# # Hello Ashutosh
# # After Function

# # Using *args and **kwargs makes the decorator
# # work with any function signature.

# def decorator(func):

#     def wrapper(*args, **kwargs):
#         print("Before Function")

#         func(*args, **kwargs)

#         print("After Function")

#     return wrapper


# @decorator
# def add(a, b):
#     print(a + b)


# add(10, 20)

# # Output:
# # Before Function
# # 30
# # After Function

# # If the original function returns a value,
# # the decorator should return it too.

# def decorator(func):

#     def wrapper(*args, **kwargs):

#         result = func(*args, **kwargs)

#         return result

#     return wrapper


# @decorator
# def add(a, b):
#     return a + b


# print(add(2, 3))

# # Output:
# # 5

# # Multiple decorators can be stacked.

# def A(func):

#     def wrapper():
#         print("A Before")

#         func()

#         print("A After")

#     return wrapper


# def B(func):

#     def wrapper():
#         print("B Before")

#         func()

#         print("B After")

#     return wrapper


# @A
# @B
# def greet():
#     print("Hello")


# greet()

# # Equivalent to:
# # greet = A(B(greet))

# # Output:
# # A Before
# # B Before
# # Hello
# # B After
# # A After

# # Decorators can accept their own arguments.

# def repeat(n):

#     def decorator(func):

#         def wrapper():

#             for _ in range(n):
#                 func()

#         return wrapper

#     return decorator


# @repeat(3)
# def hello():
#     print("Hello")


# hello()

# # Output:
# # Hello
# # Hello
# # Hello

# # Real-world example: Logging

# def logger(func):

#     def wrapper(*args, **kwargs):

#         print(f"Calling {func.__name__}")

#         return func(*args, **kwargs)

#     return wrapper


# @logger
# def greet():
#     print("Hello")


# greet()

# # Output:
# # Calling greet
# # Hello

# # Important Mental Model

# @decorator
# def greet():
#     print("Hello")

# # Python internally does:

# def greet():
#     print("Hello")

# greet = decorator(greet)

# # Decorators are just functions
# # that take a function and return another function.