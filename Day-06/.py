from collections import defaultdict
l = list(map(int,input().split()))
def val():
    return 0

d = defaultdict(val)

for i in l:
    d[i]+=1

mx = 0
for i in d:
    if d[i]>len(l)//2:
        mx=i

print(mx)


c = 1
r = l[0]

for i in l[1:]:
    if i == r:
        c += 1
    else:
        if not c:
            c -= 1
        if c == 0:
            c=1
            r = i

print(r)






