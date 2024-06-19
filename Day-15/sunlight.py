l = [3,5,9,6,8,10]
i = 0
j = 1
c = 0
while j!=len(l):
    if l[i]<l[j]:
        j+=1
        i+=1
        c+=1
    else:
        i=j
        j+=1
print(c)
c=0
l = l[::-1]
i = 0
j = 1
while j!=len(l):
    if l[i]<l[j]:
        j+=1
        i+=1
        c+=1
    else:
        i=j
        j+=1
print(c)
