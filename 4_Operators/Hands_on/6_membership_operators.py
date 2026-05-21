# Membership Operators
# Membership operators are used to check whether
# a value exists inside a sequence.

# Operators:
# in
# not in

# Example with list
numbers = [1, 2, 3, 4, 5]

# Checks if value exists in list
print("in", 3 in numbers)

# Checks if value does NOT exist in list
print("not in", 10 not in numbers)

# Example with string
name = "Ashutosh"

print("A" in name)
print("z" in name)

# Example with tuple
colors = ("red", "green", "blue")

print("green" in colors)
print("yellow" not in colors)

# Example with dictionary
student = {
    "name": "Ashu",
    "age": 21
}

# In dictionary, membership checks KEYS by default
print("name" in student)
print("Ashu" in student)

# To check values
print("Ashu" in student.values())

# Membership operators are commonly used in conditions