# Identity Operators
# Identity operators are used to check whether
# two variables point to the same object in memory.

# Operators:
# is
# is not

x = [1, 2, 3]
y = x

# y refers to the same object as x
print("is", x is y)

# Checks if both variables are NOT the same object
print("is not", x is not y)

# Different objects with same values
a = [1, 2, 3]
b = [1, 2, 3]

# Values are same
print("Equal", a == b)

# But memory locations are different
print("Identity", a is b)

# So:
# == checks values
# is checks memory/object identity

# More examples
num1 = 100
num2 = 100

print(num1 is num2)

# None comparison
value = None

print(value is None)
print(value is not None)

# Identity operators are commonly used with None