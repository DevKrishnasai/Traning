from collections import defaultdict
def val():
    return 0

s = input()
n = int(input())
sub = ""
for i in range(n):
    c,j=input().split()
    if c=="L":
        sub+=s[int(j)]
    else:
        sub+=s[-1*int(j)]

print(sub)
d1=defaultdict(val)

for x in range(len(sub)):
    d1[x]+=1

l = []
for x in range(len(s)-len(sub)+1):
    l.append(s[x:x+len(sub)])
print(l)
f = 0
sub = sorted(sub)
sub = "".join(sub)
for j in l:
    a = sorted(j)
    a = "".join(a)
    if a==sub:
        f=1
        break
if f:
    print("yes")
else:
    print("no")

