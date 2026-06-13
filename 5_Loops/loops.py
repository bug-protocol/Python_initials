# Loops are used to repeat a block of code.


# 1. FOR LOOP

# Used for iterating over a sequence
# (list, tuple, string, range, etc.)

for i in range(5):
    print(i)


# range(start, stop, step)

for i in range(1, 10, 2):
    print(i)


# Loop through list

nums = [10, 20, 30]

for n in nums:
    print(n)


# Loop through string

for ch in "Python":
    print(ch)


# 2. WHILE LOOP

# Runs until condition becomes False

count = 1

while count <= 5:
    print(count)
    count += 1


# Infinite loop

# while True:
#     print("Running forever")


# 3. BREAK

# Stops loop completely

for i in range(10):

    if i == 5:
        break

    print(i)


# 4. CONTINUE

# Skips current iteration

for i in range(5):

    if i == 2:
        continue

    print(i)


# 5. PASS

# Placeholder for future code

for i in range(3):
    pass


# 6. ELSE WITH LOOPS

# else runs only if loop finishes normally
# (without break)

for i in range(5):
    print(i)

else:
    print("Loop completed")


# 7. NESTED LOOPS

for i in range(3):

    for j in range(2):
        print(i, j)


# 8. ENUMERATE

# Gives index + value together

fruits = ["apple", "banana", "mango"]

for index, value in enumerate(fruits):
    print(index, value)


# 9. ZIP

# Loop through multiple lists together

names = ["A", "B", "C"]
marks = [90, 80, 70]

for n, m in zip(names, marks):
    print(n, m)


# 10. LIST COMPREHENSION

# Short way to create lists

squares = [x*x for x in range(5)]

print(squares)


# With condition

evens = [x for x in range(10) if x % 2 == 0]

print(evens)


# IMPORTANT LOOP TRICKS

# Reverse loop

for i in range(5, 0, -1):
    print(i)


# Loop through dictionary

data = {"a": 1, "b": 2}

for key, value in data.items():
    print(key, value)


# TIME COMPLEXITY

# Single loop        -> O(n)
# Nested loops       -> O(n^2)
# Independent loops  -> O(n * m)


# MOST IMPORTANT FOR DSA

# range()
# enumerate()
# break
# continue
# nested loops
# list comprehension
# dictionary iteration
# zip()