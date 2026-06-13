# *args and *kwargs
# these are defined to use unknown number of arguments
# *args => arbitrary arguments

def func(*val):
    print("The youngest child is " + val[2])

func("Rahul", "Steve", "Krish")

# **kwargs => Arbitrary Keyword Arguments

# arguments are stored in the form of dictionary
# allows a function to accept any number of keyword arguments
# we can use * to unpack a list and ** to unpack a dictionary

