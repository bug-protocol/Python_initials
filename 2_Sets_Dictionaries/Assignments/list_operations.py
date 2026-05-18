# list
ls = [1, 33, 56, 1001, 768]

# Appending to the end

ls.append(89)
print(ls)

# inserting 39 at the beginning of the list

ls.insert(0, 39)
print(ls)

# appending ls2 in ls
ls2 = [77,66,44]

ls.extend(ls2)
print(ls)


# Add [99,88] as a single nested element inside the list.

ls3 = [99, 88]
ls.append(ls3)
print(ls)

# Insert 'Apple' at position 2.

ls.insert(2, "Apple")
print(ls)

#Replace 'Apple' with 'Pineapple'.

ls[2] = "Pineapple"
print(ls)

# Remove the element present at position 4.
ls.pop(4)
print(ls)

# Remove 'Pineapple' from the list.
ls.remove("Pineapple")
print(ls)
