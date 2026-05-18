# We have our list as

ls = [1,2,3,4,5,6,7,8]
z = 9

# Using two loops => O(n^2)
ans = ()
for i in range(len(ls)):
    for j in range(i+1, len(ls), 1):
        if ls[i]+ls[j]==z:
            ans = ans + ((ls[i],ls[j]),)

print(ans)

# Using sets

ls2 = set(ls)
ans2 = []
for i in ls:
    val = z - i
    if val in ls2:
        ans2.append((i,val))
        ls2.remove(i)
        ls2.remove(val)

print(tuple(ans2))