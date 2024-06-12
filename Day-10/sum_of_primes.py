from math import sqrt


def isPrime(a):
    flag=0
    for i in range(2,int(sqrt(a))+1):
        if a%i==0:
            flag=1
            break
    if a in [0,1]:
        return False
    return flag==0 and True


l = list(map(int,input().split()))
s = 0
for i in range(len(l)-1):
    for j in range(l[i+1]-1,l[i],-1):
        print(j)
        if isPrime(j):
            s+=j
            break

print(s)

