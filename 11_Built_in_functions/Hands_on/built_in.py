#common built in python functions
# Type Conversion

int("10")        # 10
float("3.14")    # 3.14
str(100)         # "100"
list("abc")      # ['a', 'b', 'c']
tuple([1, 2])    # (1, 2)
set([1, 1, 2])   # {1, 2}
dict()
bool(1)          # True

# Maths
abs(-5)          # 5
round(3.14159, 2) # 3.14
pow(2, 3)        # 8
min(1, 2, 3)     # 1
max(1, 2, 3)     # 3
sum([1, 2, 3])   # 6
divmod(10, 3)    # (3, 1) => returns both quotient and reminder in a tuple

# Iterables
len([1, 2, 3])       # 3
sorted([3, 1, 2])    # [1, 2, 3]
reversed([1, 2, 3])
print(list(enumerate(['a', 'b'])))  # => when needed both index and value while iterating
print(list(zip([1, 2], ['a', 'b'])))    # => combines elements from multiple iterables position-wise
map(str, [1, 2, 3])
filter(lambda x: x > 0, [-1, 2, 3])
any([False, True])   # True
all([True, True])    # True