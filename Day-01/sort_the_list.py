l1 = list(map(int,input().split(" ")))
l2 = list(map(int,input().split(" ")))


# method 1
# l1.extend(l2)
# print(sorted(l1))


# method 2
i= 0
j = 0
l = []
while len(l1)>i and len(l2)>j:
    if l1[i]>l2[j]:
        l.append(l2[j])
        j+=1
    else:
        l.append(l1[i])
        i+=1

while len(l1)>i:
    l.append(l1[i])
    i+=1


while len(l2)>j:
    l.append(l2[j])
    j+=1

print(l)
