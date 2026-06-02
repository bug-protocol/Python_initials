# *args and *kwargs
# these are defined to use unknown number of arguments
# *args => arbitrary arguments

def func(*val):
    print("The youngest child is " + val[2])

func("Rahul", "Steve", "Krish")