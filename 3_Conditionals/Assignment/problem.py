# Consider a list 

arr = [4, 4, 1, 1, 1, 2, 3, 3, 3]

# Sort this list in a manner such that elements with higher frequency are arranged first,
# and in case of similar frequency the element with the greater value comes first.

# Solution

# create a dictionary which going to store key as element and its frequency as its value

freq = {}

for num in arr:

    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1

arr.sort(key=lambda x: (-freq[x], -x))

print(arr)