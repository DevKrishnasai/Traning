#can take again
n = int(input())
m = []
for i in range(n):
    m.append(input())
s = input()
temp=0

for i in s:
    if i in m[temp]:
        temp+=1
        if temp%n==0:
            temp=0
    else:
        print("no")
        exit(0)
print("yes")

#cannot take again
n = int(input())
t = []
# m = []

for i in range(n):
    # m.append(input())
    # t.append(list(m[-1]))
    t.append(list(input()))

s = input()
temp=0

for i in s:
    if i in t[temp]:
        t[temp].remove(i)
        temp+=1
        if temp%n==0:
            temp=0
    else:
        print("no")
        exit(0)
print("yes")
