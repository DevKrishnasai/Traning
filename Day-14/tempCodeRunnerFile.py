l = list(map(int,input().split()))
n = int(input())

m = [[0]*(n+1) for _ in range(len(l))]

for i in range(len(l)):
    for j in range(n+1):
        if i == 0:
            m[i][j]=j
        elif j<i: