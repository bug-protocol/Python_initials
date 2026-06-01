# first q
s = "Hello"
print(id(s))

s += "World"
print(id(s))

# second ques

print(0 or [] or {})
print("" or "hello")
print([] and 100)

# Explanation

# or => returns first truthy value and if there is none returns last value
# and => returns the first falsy value and if there is none falsy it returns last value

 # why
 # because python enables elegant shortcuts

 # like suppose we've used these conditionals 
 # for or => we'll try to counter for first truthy value and nothing else matters
 # for and => we'll try to counter for the first falsy value and nothing else matters 


 # new quest

print(bool("False"))

# why is it returning true => because every non - empty string is ofcourse gonna give you true


# new quest 

nums = [1,2,3,4]

for x in nums:
    nums.remove(x)

print(nums)

# explanation
# we'll expect [] but instead the iterations would be something like
# nums = [1, 2, 3, 4]
#         0  1  2  3
# now in this iteration we removed index 0 and the iterator has finally moved onto index one

# BUT...during second iteration
# nums = [2, 3, 4]
#         0  1  2
# so it'll now skip 0th index and remove the  1st index

# Third iteration
# nums = [2, 4]
#         0  1


# final ques
a = "hello"
b = "hello"

print(a is b)

a = "hello world this is long"
b = "hello world this is long"

print(a is b)

# Shallow and Deep Copy

ls = [[0] * 3] * 3

print(ls)

ls[0][0] = 1

# pause and confuse

print(ls)

# Why
# [[0,0,0]=> literally independent slots] but when we're doing *3 on this...we're getting instance of
# 3 different objects pointing towards the same address. 