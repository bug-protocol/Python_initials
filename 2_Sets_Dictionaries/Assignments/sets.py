python_students = {"Rahul","Amit","Sneha","John"}
sql_students = {"John","Sneha","David","Meena"}
aws_students = {"Rahul","David","Kiran"}

python_sql = python_students | sql_students
print(python_sql)

int1 = python_students & sql_students
int2 = python_students & aws_students
int3 = sql_students & aws_students

int4 = int1 | int2 | int3
print(int4)
# 1. Students in both Python and SQL
both_p_sql = python_students & sql_students
print(both_p_sql)
# 2. Students in all 3 courses
all_3 = python_students | sql_students | aws_students
print(all_3)

# 3. Students only in Python
python = python_students.difference(sql_students | aws_students)
print(python)

# 4. Total unique students
all_3 = python_students | sql_students | aws_students
print(all_3)

# 5. Students not enrolled in AWS
not_in_aws = python_sql.difference(aws_students)
print(not_in_aws)

# 6. Students in more than 2 courses.

more_than_2 = python_students & sql_students & aws_students

# 7. Students whose name starts with 'Ra'
for i in all_3:
    if i.startswith("Ra"):
        print(i)

# 8. Students whose name ends with 'na' or 'an'
for i in all_3:
    if i.endswith("an") | i.endswith("na"):
        print(i)




# Frequency Counter
data = [1,2,2,3,4, 4, 4, 7 , 7 ,7,8,9]

# unique values
st = set(data)
print(st)

# duplicate values
encounter = set()
visited = set()
ans = list()
for i in data:
    if i in encounter:
        if i in visited:
            continue
        else:
            ans.append(i)
            visited.add(i)

    else:
        encounter.add(i)

print(ans)

# frequency of each value

freq = [0] * int(1e5)
for i in data:
    freq[i] += 1

storefreq = set()
for i in data:
    storefreq.add((i,freq[i]),)
print(storefreq)

# using list and set
cal = list()
for i in st:
    cal.append([i,data.count(i)],)

print(cal)

data = [1,2,2,3,4, 4, 4, 7 , 7 ,7,8,9]

from collections import Counter
x = dict(Counter(data))
print(x)

# using sort

# cal2 = data.copy()
# cal2.sort()
# ans2 = list()
# count = 1
# for i in range(len(cal2)-1):
#     if cal2[i]==cal2[i+1]:
#         count += 1
#     else:
#         ans2.append([cal2[i], count])
#         count = 1

#     print(i)

# ans2.append([cal2[i+1], count])

# print(ans2)