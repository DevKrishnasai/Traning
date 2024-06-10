
m=[[0,1,1,1,0,1],[0,1,0,1,0,0],[1,0,1,1,0,0],[0,0,0,1,1,1],[1,1,0,0,0,1],[1,1,1,0,1,0]]
n=len(m)
p,q = list(map(int,input().split()))


for i in range(n):
    for j in range(n):
        print(m[i][j],end=' ')
    print()

count=0
def fun(i,j):
    if m[i][j]==0:
        return
    else:
        m[i][j]=0

    if i>0:
        fun(i-1,j)
    if i<n-1:
        fun(i+1,j)
    if j>0:
        fun(i,j-1)
    if j<n-1:
        fun(i,j+1)




fun(p,q)
c=0
for i in range(n):
    for j in range(n):
        if m[i][j]==1:
            c+=1
print()
for i in range(n):
    for j in range(n):
        print(m[i][j],end=' ')
    print()
print(c)
