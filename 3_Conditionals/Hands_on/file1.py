# Basic logical conditionals:
# a == b ==> Equals
# a != b ==> not equal to
# a < b ==> less than
# a > b ==> greater than
# a <= b ==> less than equal to 
# a >= b ==> more than equal to

a = input()
b = input()

print("the value of b", b)
if a < b:
    print("a is less than b")
else:
    print("a is greater than b")

# elif keyword

x = input()
y = input()

if x < y:
    print("x is less than y")
elif x == y:
    print("x and y are equal")

    

