# LIST COMPREHENSION

nums = [1, 2, 3, 4, 5]

squares = [x * x for x in nums]

print(squares)

# Output
# [1, 4, 9, 16, 25]

# Equivalent

squares = []

for x in nums:
    squares.append(x * x)


# With Condition

nums = [1, 2, 3, 4, 5, 6]

evens = [x for x in nums if x % 2 == 0]

print(evens)

# Output
# [2, 4, 6]


# If Else

nums = [1, 2, 3, 4]

result = ["Even" if x % 2 == 0 else "Odd" for x in nums]

print(result)

# Output
# ['Odd', 'Even', 'Odd', 'Even']


# Nested Loop

pairs = [(i, j) for i in range(2) for j in range(3)]

print(pairs)

# Output
# [(0,0), (0,1), (0,2), (1,0), (1,1), (1,2)]


# DICTIONARY COMPREHENSION

nums = [1, 2, 3, 4]

d = {x: x * x for x in nums}

print(d)

# Output
# {1:1, 2:4, 3:9, 4:16}


# With Condition

d = {x: x * x for x in nums if x % 2 == 0}

print(d)

# Output
# {2:4, 4:16}


# Swap Keys and Values

d = {"a": 1, "b": 2}

swapped = {v: k for k, v in d.items()}

print(swapped)

# Output
# {1:'a', 2:'b'}


# Quick Rule

# List Comprehension
# [expression for item in iterable if condition]

# Dict Comprehension
# {key:value for item in iterable if condition}