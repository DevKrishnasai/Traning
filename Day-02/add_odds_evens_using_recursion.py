a = list(map(int,input().split()))
b = list(map(int,input().split()))

def result(i,o=0,e=0):
    if i==len(a):
        return (e,o)
    if a[i]%2==0:
        e+=a[i]

    if b[i]%2!=0:
        o+=b[i]
    return result(i+1,o,e)

print(result(0))





