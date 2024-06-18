l = list(map(int,input().split()))
l1 = []
l2 = []
i = 0
j = len(l)-1
mx = 0
mx1 = 0
while i!=len(l) and j!=-1:
    l1.append(max(l[i],mx))
    mx = l1[-1]
    l2 = [max(mx1,l[j])] + l2
    mx1 = l2[0]
    i+=1
    j-=1


print(l1,l2)
s = 0
for i in range(len(l)):
    m = min(l1[i],l2[i])
    s+=m-l[i]
print(s)

# 2 5 2 3 6 7 1 0 5 7
