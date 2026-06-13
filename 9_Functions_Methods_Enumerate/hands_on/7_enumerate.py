# enumerate()
# used when you need both index and value while iterating
# returns an enumerate object containing (index, value) pairs

# Syntax

# enumerate(iterable, start=0)


# Basic Example

fruits = ["apple", "banana", "mango"]

for i, fruit in enumerate(fruits):
    print(i, fruit)

# Output
# 0 apple
# 1 banana
# 2 mango


# Custom Starting Index

fruits = ["apple", "banana", "mango"]

for i, fruit in enumerate(fruits, start=1):
    print(i, fruit)

# Output
# 1 apple
# 2 banana
# 3 mango


# Converting to List

fruits = ["apple", "banana", "mango"]

print(list(enumerate(fruits)))

# Output
# [(0, 'apple'), (1, 'banana'), (2, 'mango')]


# Without enumerate()

fruits = ["apple", "banana", "mango"]

for i in range(len(fruits)):
    print(i, fruits[i])


# With enumerate() (Preferred)

for i, fruit in enumerate(fruits):
    print(i, fruit)


# Common Interview Points

# returns (index, value) pair
# default starting index is 0
# start parameter can change the starting index
# cleaner than using range(len())
# returns an enumerate object