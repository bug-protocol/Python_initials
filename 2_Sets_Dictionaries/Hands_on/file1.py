# set is unordered collection of unique elements
arr = {1, 3, 2, 5, 4, 5}
print(arr)

# No duplicates
# output becomes sorted
# mutable
# unchangeable means can not allocate different values

#Set Methods

# Add element ==> add the element to its particular position in the sorted collection
arr.add(7)
arr.add(6)
print(arr)

# Remove Method ==> Removes all existing elements in the array, and will throw error if element
# is not found

arr.remove(5)
print(arr)

# True and 1 are considered same in the sets and are considered duplicates if they are present 
# in the same set

# Similarly False and 0 are considered the same and will be considered as duplicates.
arr.add(True)
print(arr)

# Length of the set 
print(len(arr))

# set items can be of any data type

brr = {1, 2, 3, "Dog", "Cat", 5}
print(brr)

# The set() constructor ==> used to construct set

s = set(("apple", "orange"))
print(type(s))



# Accessing items in set

# Loop through it
for i in arr:
    print(i)

# check if 2 is in this set
print(2 in arr)


# update method ==> adding brr into arr...arr updates

arr.update(brr)
print(arr)
print(brr)

# the obejct in update() doesn't need to be a set, it can be any iterable(list, dict, tuple)

# Discard Method => unlike remove doesn't results in an error if item is not found

arr.discard(2)
print(arr)

arr.discard(8)
print(arr)

arr.pop()
print(arr)

# using pop it can remove any item randomly --> as set is unordered you do not know which item is gonna get removed


# Clear method => clear the set

# del keyword will remove the set completely
del(brr)


# Joining sets

# Union => returns a new set containing all the items from both sets
x = {2, 3, 5}
y = {1, 4}
z = x.union(y)
print(z)

# we can use "|" instead of union and we'll still get the same result
z = x | y
print(z)

# to join multiple sets

a = {9, 8, 6}
fin = x | y | a
print(fin)

# using union we can join any kind of data types but using "|" we can only join sets

# Intersection ==> it'll return only those elements which are common in both sets
# we can use "&" and we'll still get the same result
# same goes here "&" for sets only can't join other data types

x3 = arr & z
print(x3)

# intersection_update() ==> if you don't want to create a new set but just want to update the old set we can use intersection_update

# difference() => it'll return only those elements which are not present in the second set
a1 = {1,2 ,3, 4, 5}
a2 = {1, 2 , 3}
a3 = a1.difference(a2)
print(a3)
# "-" => could be used as alternative of difference
