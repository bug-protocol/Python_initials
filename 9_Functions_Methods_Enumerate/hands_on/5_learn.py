# Generators
# generators produce values one at a time instead of storing everything in memory
# useful for large datasets and sequences

# yield keyword
# yield returns a value and pauses the function
# execution resumes from the same point on the next call

def nums():
    yield 1
    yield 2
    yield 3

g = nums()

print(next(g))   # 1
print(next(g))   # 2
print(next(g))   # 3


# Generator vs Return

def func():
    return [1, 2, 3]

# returns entire list at once


def gen():
    yield 1
    yield 2
    yield 3

# returns values one by one


# Iterating over a Generator

def count(n):
    for i in range(n):
        yield i

for x in count(5):
    print(x)


# Generator Expression
# similar to list comprehension but uses ()

squares = (x * x for x in range(5))

print(next(squares))   # 0
print(next(squares))   # 1


# List Comprehension vs Generator Expression

lst = [x * x for x in range(1000000)]
# stores all values in memory

gen = (x * x for x in range(1000000))
# generates values on demand


# Common Interview Points

# generators use yield instead of return
# generator objects are iterable
# values are generated lazily (on demand)
# memory efficient for large data
# next() gets the next value
# StopIteration is raised when generator is exhausted
# generator expressions use ()
# list comprehensions use []