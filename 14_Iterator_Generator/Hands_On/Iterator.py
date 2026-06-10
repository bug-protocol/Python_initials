# Iterator allows you to traverse through elements one at a time
# Contains two methods:-
# __iter__() => returns the iterator object itself
# __next__() => returns the next value

arr = [1, 2, 3, 4, 5]

it = iter(arr)
# iterator created

print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))