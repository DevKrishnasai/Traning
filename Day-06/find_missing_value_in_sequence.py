n = int(input())
l = list(map(int,input().split()))

f = n*(n+1)//2 - sum(l)

print(f)
