# Python Regex (re)

import re

# search() -> first match anywhere

x = re.search(r"\d+", "abc123").group()
if x:
    print(x)
else:
    print("not found")
# Output
# 123


# findall() -> all matches

y = re.findall(r"\d+", "a1 b22 c333")
if y:
    print(y)
else:
    print("not found")
# Output
# ['1', '22', '333']


# split() -> split using pattern

z = re.split(r"\s", "Hello World Python")
if z:
    print(z)
else:
    print("Not found")
# Output
# ['Hello', 'World', 'Python']


# sub() -> replace matches

a = re.sub(r"\s", "-", "Hello World")
if a:
    print(a)
else:
    print("not found")
# Output
# Hello-World


# Common Special Characters

# \d    digit (0-9)
# \D    non-digit

# \w    letter, digit, _
# \W    not letter, digit, _

# \s    whitespace
# \S    non-whitespace

# .     any character

# ^     start of string
# $     end of string


# Character Sets

# [abc]      a or b or c
# [a-z]      lowercase letters
# [A-Z]      uppercase letters
# [0-9]      digits
# [^abc]     not a, b, c


# Quantifiers

# *      0 or more
# +      1 or more
# ?      0 or 1

# {n}      exactly n times
# {n,}     n or more times
# {m,n}    m to n times


# Examples

re.findall(r"\d{3}", "123 45 678")

# Output
# ['123', '678']


re.findall(r"[A-Z][a-z]+", "Rahul Steve krish")

# Output
# ['Rahul', 'Steve']


# Groups

m = re.search(r"Name: (\w+)", "Name: Rahul")

m.group(1)

# Output
# Rahul


# Match Object

m = re.search(r"\d+", "abc123")

m.group()      # matched text
m.start()      # start index
m.end()        # end index


# Raw String

r"\d+"

# r"" prevents Python from treating \ as an escape character

# search()  -> first match
# findall() -> all matches
# split()   -> split string
# sub()     -> replace matches
# group()   -> matched value
# ()        -> capture group
# []        -> character set
# ^         -> starts with
# $         -> ends with
# r""       -> raw string