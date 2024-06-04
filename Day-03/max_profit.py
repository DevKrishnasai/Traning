
#two pointer
l = list(map(int,input().split()))
i = 0
j = 1
mx = 0
while j<len(l):
    if l[i]<l[j]:
        mx = max(mx,l[j]-l[i])
    else:
        i=j
    j+=1
print(mx)

