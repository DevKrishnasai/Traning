import datetime as date
n = int(input())
def prime(a):
    c=0
    #(a//2)+1 needed to reduce iterations
    for i in range(2,(a//2)+1):
        if a%i==0:
            c+=1
            break
    return c==0 and True

c = prime(n)
if c:
    print(n)
else:
    a = n+1
    while True:
        c = prime(a)
        if c:
            print(a)
            break
        a+=1



