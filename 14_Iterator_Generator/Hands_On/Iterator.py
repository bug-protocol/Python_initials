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
print(next(it))  # if no element is present gives us StopIteration  

class MyNumbers:
  def __iter__(self):  # defining the iterator
    self.a = 1
    return self

  def __next__(self):  # printing every next statement after it
    if self.a <= 10:
        x = self.a
        self.a += 1
        return x
    else:
       raise StopIteration # to stop the iteration after limit is reached

myclass = MyNumbers()  
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))