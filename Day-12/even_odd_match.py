l1 = [6,3,2,9,4,7]
l2 = [8,7,5,3,6,9]
x = []

def odd(l,i,j=0):
    if j==len(l2):
        x.append(sum(l))
        return
    if l2[j]%2:
        l.append(l1[i]+l2[j])
    odd(l,i,j+1)

def recu(i):
    if i==len(l1):
        return
    if not l1[i]%2:
        odd([],i)
    recu(i+1)
recu(0)

print(x)
