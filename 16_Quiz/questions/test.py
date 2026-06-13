# Q. 1

import copy

def func(lst=[[]]):
    x = copy.copy(lst)
    x[0].append(1)
    return x

print(func())
print(func())

# Q. 2

def gen(lst):
    for item in lst:
        yield item

nums = [1,2,3]

g = gen(nums)

print(next(g))

nums.append(4)

print(list(g))


# here from line g = gen(nums) generator is initiated but it's not yet working
# now when next print function runs it gives 1
# and the next thing would be [2, 3, 4]

# Q..3

nums = iter([10, 20, 30])

print(next(nums))

e = enumerate(nums)

print(next(e))
print(list(e))

# initially iterator is at 10
# when print(next(nums)) runs it gives us 10

# now when enumerated 0 -> 20
                    # 1 -> 30



# Q--> 4

a = [1,2,3,4]

# print(id(a))
b = a

a[:] = []
# a = []
# print(id(a))

print(a)
print(b)

# when slicing happended the variable a is pointing to the original address of a
# hence when a was modified b also got modified

# Q---> 5

a = [[0] * 3] * 3

a[0][0] = 1

print(a)


# Q---> 6

def outer(x):
    def inner(y=x):
        return y
    x = 100
    return inner

f = outer(5)

print(f())

# default arguments are applied here 

# Q --> 7

import re

count = 0

def func():
    count = len(re.findall(r"\d+", "1 22 333"))
    return count

func()

print(count)

# Here the output will be 0, because func() will definitely
# give the value of count as 3 as re.findall will give
# ["1", "22", "333"]
# but it's in function and we didn't do count = func() hence
# whatever was in function disappeared and the print statement 
# will inherit global value and hence it'll be 0