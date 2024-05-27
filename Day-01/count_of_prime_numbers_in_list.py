from math import sqrt

#method 1
def prime(a):
    flag=0
    for i in range(2,int(sqrt(a))+1):
        if a%i==0:
            flag=1
            break
    if a in [0,1]:
        return False
    return flag==0 and True


n = input()
c=0
for i in n:
    a = prime(int(i))
    if a:
        c+=1
print(c)

# method 2
c=0
for i in n:
    if i in "2357":
        c+=1
print(c)
