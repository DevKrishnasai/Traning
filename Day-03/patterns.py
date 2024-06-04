#Method 1 (complex to understand)
n = int(input())
j = 1
for i in range(n):
    m = n-2
    if i in [0,n-1]:
        s="* "*n
    else:
        s="* "
        while m>0:
            s+=str(j)+" "
            m-=1
            j+=1
        s+="*"
    print(s)

#Method 2 (easy to understand)
n = int(input())
c = 1
k = n-2
for i in range(n):
    if i == 0 or i==n-1:
        print("* "*n)
    else:
        s = list(map(str,range(c,c+k)))
        l = " ".join(s)
        print("*",l,"*")
        c+=k

