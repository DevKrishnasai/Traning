def fun(i,j,p,t):
    if p==len(word):
        return 1
    if i<0 or j<0 or j>n or i>n or m[i][j]!=word[p]:
        return
    else:
        m[i][j]="#"

    print(m[i][j],word[p])
    if p<len(word):
        t = fun(i-1,j,p+1,t)
        t = fun(i+1,j,p+1,t)
        t = fun(i,j-1,p+1,t)
        t = fun(i,j+1,p+1,t)
    return t




n = int(input())
word = input()
m = []
l = []
for i in range(n):
    x = list(map(str,input().split()))
    m.append(x)
    l.append(x)

x = word[0]
for i in range(len(m)):
    for j in range(len(m)):
        if m[i][j]==x:
            fun(i,j,1,0)

for i in range(n):
    for j in range(n):
        print(m[i][j],end=' ')
    print()

# print("yes")
