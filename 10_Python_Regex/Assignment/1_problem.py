import re
str = "4304, This is the value of gold today. Steve is not gonna buy anything today."

pattern = re.compile(r'\bis')
match = pattern.finditer(str)
for it in match:
    print(it)

# Question 1
text = "Contact us at support@test.com or admin123@gmail.com"

pattern1 = re.compile(r'[\w]\w*[@]\w*[.][c][o][m]')
findem = pattern1.finditer(text)
for it in findem:
    print(it)

# Question 2
passwords = [
    "Password@123",
    "password123",
    "PASSWORD@123",
    "Pass123",
]

pattern2 = re.compile(r'^(?=.*[A-Z])(?=.*[a-z])(?=.*[1-9])(?=.*[^A-Za-z0-9]).{8,}')
for pwd in passwords:
    print(pwd, bool(pattern2.match(pwd)))

# Question 3
dates = "Meeting on 12-05-2026 and another on 2026-06-01"

pattern3 = re.compile(r'[\d][\d][-][\d][\d][-][\d][\d][\d][\d] | [\d][\d][/][\d][\d][/][\d][\d][\d][\d] | [\d][\d][\d][\d][-][\d][\d][-][\d][\d]')
date = pattern3.finditer(dates)
for it in date:
    print(it)


# Question 4
trimspaces = "Hello     World\t\tPython"

pattern4 = re.sub(r'\s+', ' ', trimspaces)
print(pattern4)

# Question 6
logTime = """
2026-06-01 10:23:45 ERROR Database connection failed
2026-06-01 10:24:12 INFO User login successful
"""

pattern6 = re.compile(r'(\d{4}-\d{2}-\d{2}\s+\d{2}:\d{2}:\d{2})\s+(\w+)\s+(.*)')
print(pattern6)
# Question 8
curr = "Revenue was $1,200,300.50, profit ₹500,000 and loss €300"

pattern8 = re.compile(r'[$₹€]\d[\d,]*[.]?\d*')
findcurr = pattern8.finditer(curr)
for it in findcurr:
    print(it)