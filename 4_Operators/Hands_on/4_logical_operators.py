# Logical Operators
# Logical operators are used to combine multiple conditions.
# They also return True or False.

x = 12
y = 5
z = 20

# AND operator
# True only if both conditions are True
print("AND", x > y and z > x)

# OR operator
# True if at least one condition is True
print("OR", x < y or z > x)

# NOT operator
# Reverses the result
print("NOT", not(x > y))

# More examples

age = 20
has_id = True

# Person can enter only if age >= 18 AND has_id is True
print(age >= 18 and has_id)

marks = 35

# Pass if marks >= 33 OR has sports quota
sports_quota = False
print(marks >= 33 or sports_quota)

is_raining = True

# NOT converts True to False
print(not is_raining)

# Logical operators are mostly used in if-else conditions