l = list(map(int, input().split()))
n = int(input())

m = [-1] * (n+1)
m[0]=0
for i in l:
    for j in range(i,n):
        if j >= i:
            s = j-i
            if m[s]!=-1:
                if m[j]!=-1:
                    m[j]=min(m[s]+1,m[j])
                else:
                    m[j]=m[s]+1



print(m)
print(m[-1])
