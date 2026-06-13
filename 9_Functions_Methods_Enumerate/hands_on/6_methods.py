# Important Python Methods for DSA

# LIST METHODS

arr = [3, 1, 2]

arr.append(4)          # add at end
arr.extend([5, 6])     # add multiple elements
arr.insert(1, 10)      # insert at index

arr.pop()              # remove last element
arr.pop(1)             # remove by index
arr.remove(10)         # remove first occurrence

arr.index(2)           # find index
arr.count(1)           # frequency of element

arr.sort()             # ascending sort
arr.sort(reverse=True) # descending sort
arr.reverse()          # reverse list

arr.copy()             # shallow copy
arr.clear()            # remove all elements


# STRING METHODS

s = "hello world"

s.upper()
s.lower()
s.capitalize()
s.title()

s.strip()              # remove spaces from ends
s.replace("world", "python")

s.split()              # string -> list
"-".join(["a", "b"])   # list -> string

s.startswith("he")
s.endswith("ld")

s.find("o")            # -1 if not found
s.index("o")           # error if not found

s.count("l")

s.isdigit()
s.isalpha()
s.isalnum()


# SET METHODS

st = {1, 2, 3}

st.add(4)
st.update([5, 6])

st.remove(2)           # error if absent
st.discard(2)          # no error if absent

st.pop()               # removes arbitrary element

st.union({4, 5})
st.intersection({2, 3})
st.difference({2})

st.issubset({1, 2, 3, 4})
st.issuperset({1, 2})


# DICTIONARY METHODS

d = {"a": 1, "b": 2}

d.get("a")
d.get("c", 0)

d.keys()
d.values()
d.items()

d.update({"c": 3})

d.pop("a")
d.popitem()            # removes last key-value pair

d.setdefault("x", 0)

d.copy()
d.clear()


# TUPLE METHODS

t = (1, 2, 2, 3)

t.count(2)
t.index(3)


# BUILT-IN FUNCTIONS OFTEN USED IN DSA

len(arr)
sum(arr)
min(arr)
max(arr)

sorted(arr)

abs(-10)

enumerate(arr)

zip(arr, arr)

any([0, 0, 1])
all([1, 1, 1])

list("abc")
set([1, 2, 2, 3])
dict()

reversed(arr)


# COLLECTIONS (VERY IMPORTANT)

from collections import Counter
Counter("aabcc")

from collections import defaultdict
defaultdict(int)

from collections import deque
dq = deque()

dq.append(1)
dq.appendleft(0)

dq.pop()
dq.popleft()


# HEAPQ (MUST KNOW)

import heapq

heap = []

heapq.heappush(heap, 5)
heapq.heappush(heap, 1)

heapq.heappop(heap)

heapq.heapify(arr)

heapq.nlargest(3, arr)
heapq.nsmallest(3, arr)