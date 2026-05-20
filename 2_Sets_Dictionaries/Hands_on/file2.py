# Dictionary ==> stores data values in key value pairs
dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(dict)

# ordered
# changeable
# do not allow duplicates

# accessing
print(dict["brand"])
# can not have two items with same key
# len for length of the dictionary

# We can use get() for the same purpose
ele = dict.get("model")
print(ele)

# keys() ==> gets all the keys from the dictionary
print(dict.keys())

# values() ==> gets all values
print(dict.values())

# items() ==> gives all items of dictionary
print(dict.items())

# changeable

dict["year"] = 1999

# update => updates the items of the dictionary relative to the given key
dict.update({"year":2000})
print(dict.items())

# Adding items

dict["colour"] = "red"
print(dict.items())

# we can even use update to insert in the dictionary in case the relative key is not present

# Removing elements
# pop() -> removes the item with the specified key name
dict.pop("colour")
print(dict)

# popitem() ==> removes the last inserted item

# copying the dictionary

dict2 = dict(dict)
print(dict2)


# Summary

# Dictionary ==> Ordered
#                Changeable
#                No duplicate keys
#                dict constructor

# Accessing elements
# we can access elements using get() method
# keys()
# values()
# items()
# checking if "key" exists in dict => using "in"


# Change items
# update() => to update dictionary ({})

# update can be used to add items in dictionary

# remove items
# pop("key") 
# popitem() => removes last inserted element
# del => removes items as well as dictionary
# clear => empties dictionary


# Looping
# for i in dict:
    # here i will give you keys => for values you gotta dict["i"]
    # or use dict.keys(), dict.values(), dict.items()

# Copying dictionary
# using dict.copy()
# using dict() constructor

# Nested Dictionary
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

# for accessing
print(myfamily["child2"]["name"])