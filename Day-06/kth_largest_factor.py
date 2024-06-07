from math import sqrt
n = int(input())
k = int(input())
for i in range(1,int(sqrt(n))+1):
    if n%i==0:
        k-=1
        if k==0:
            print(i,n//i)
            break





