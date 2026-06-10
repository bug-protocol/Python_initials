# Generator in python is simpler way to create an iterator  

# Instead of implementing __iter__() and __next__(), we use the yield keyword.

def count(limit):
    num = 1
    while num <= limit:
        yield num
        num += 1

g = count(3)

print(next(g))
print(next(g))
print(next(g))
# print(next(g))  => StopIteration

def demo():
    print("A")
    yield 1

    print("B")
    yield 2

    print("C")
    yield 3

g = demo()

print(next(g))
print(next(g))
print(next(g))

