students = {
    "Rahul": 85,
    "Sneha": 67,
    "Amit": 67,
    "John": 45

}
# Find topper
maxi = 0
topper = str
for i in students:
    if students[i] > maxi:
        maxi = students[i]
        topper = i

print(topper)

# Find failed students (<50)

failed_st = list()
for i in students:
    if students[i] < 50:
        failed_st.append(i)

print(failed_st)

# Find students with same marks
unique_st = set()
mark_dict = dict()
for i in students:
    if students[i] in unique_st:
        mark_dict[students[i]].append(i)
    else:
        unique_st.add(students[i])
        mark_dict[students[i]] = [i]

fin_dict = dict()
for i in mark_dict:
    if len(mark_dict[i]) > 1:
        fin_dict[i] = (mark_dict[i])

print(fin_dict)

# Print Grades

for i in students.values():
    print(i)


# Merge and sort dictionary 
d1 = {"a": 3, "b": 2}
d2 = {"c": 1, "d": 4}
d2.update(d1)
print(d2)

# sort by key
print(dict(sorted(d2.items())))
# print(d3)

# sort by values
print(dict(sorted(d2.items(), key = lambda x : x[1])))

# key works as the comparator => where using lambda function as x : x[1]
# make it look like you gotta sort using values

cart = {
    "Laptop": {"price": 50000, "qty": 1},
    "Mouse": {"price": 500, "qty": 2}
}
print(cart)

# Add product
cart.update({"Keyboard" : {"price" : 400, "qty" : 5}})
print(cart)

# update quantity

cart["Keyboard"].update({"qty" : 3})
print(cart)

# Remove Product

cart.pop("Mouse")
print(cart)

# Calculate total bill
bill = 0
for i in cart:
    bill += cart[i]["price"] * cart[i]["qty"]
    # print(bill)

print(bill)

# Find most expensive Product

maxi = 0
product = str
for i in cart:
    if cart[i]["price"] > maxi:
        maxi = cart[i]["price"]
        product = i

print(product)

# Apply 10% discount if total > 50000
discount = 1/10
if bill > 50000:
    bill -= bill * discount

print(bill)