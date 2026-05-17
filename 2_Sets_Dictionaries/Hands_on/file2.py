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