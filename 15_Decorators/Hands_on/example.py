def greet():
    print("Hello World!")

greet()

# Now suppose I want that before and after printing this function I get some
# welcoming statement or anything random

# def decorators(func):

#     def inner():
#         print("Hi There!")
#         func()
#         print("We are going to learn about decorators!")

#     return inner


# @decorators
# def hello(a):
#     print(f"Hello World!,{a}")
#     # print("Hello World!")

# hello()

# # Hence decorator is a function that takes another function as an argument and returns a 
# # new function that modifies the behaviour of the original function.

# # Function with argument

def decorators2(func):
    def inner(*args, **kwargs):
        print("Function with arguments!")
        func(*args, **kwargs)
        print("The End!")

    return inner

@decorators2
def add(a, b):
    print(a+b)

# decorators2(add)(2, 3)
add(2, 3)