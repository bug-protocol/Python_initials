# the try block lets you test a block of code for errors.
# the except block lets you handle the error.
# the else block lets you execute code when there is no error.
# the finally block lets you execute code, regardless of the result of the try-and except blocks

x = 10
y = 0
try:
    print(x/y)
except ZeroDivisionError:
    print("Found zero div error")
except:
    print("div error")

# ordering matters here

x = 10
y = 2

try:
    print(x/y)
except:
    print("Error Found!")
else:  # => raised when no error or exceptions are hit
    print("NO exception found!")
finally:
    print("Execution in any case, error found or not!")

# Raising an exception

# x = 0
# if x < 10:
#     raise Exception("No numbers below 10 are valid!")

# Raising typeerror

# x = "hello"
# if not type(x) is int:
#   raise TypeError("Only integers are allowed")

# Multiple exceptions in one except
try:
    x = 34/0
except (ValueError, TypeError):
    print("Handled")
finally:
    print(y)
    
