# Lambda Functions
# anonymous (nameless) functions
# used for short, one-line functions


# Normal Function

def square(x):
    return x * x

print(square(5))


# Lambda Function

square = lambda x: x * x
print(square(5))


# Multiple Arguments

add = lambda a, b: a + b
print(add(10, 20))


# Used with sorted()

students = [("Rahul", 80), ("Krish", 95), ("Steve", 75)]

students.sort(key=lambda x: x[1])

print(students)


# Used with map()
# applies function to every element

nums = [1, 2, 3, 4]

result = list(map(lambda x: x * 2, nums))

print(result)


# Used with filter()
# keeps elements where condition is True

nums = [1, 2, 3, 4, 5, 6]

result = list(filter(lambda x: x % 2 == 0, nums))

print(result)


# Used with reduce()
# reduces list to a single value

from functools import reduce

result = reduce(lambda a, b: a + b, [1, 2, 3, 4])

print(result)


# Common Interview Points

# lambda can have any number of arguments
# lambda can have only one expression
# lambda automatically returns the result
# mostly used with map(), filter(), reduce(), sorted()
# useful for short temporary functions