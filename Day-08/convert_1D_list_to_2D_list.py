# l = list(map(int,input().split()))
# x = []
# sub = []
# for i in l:
#     if i not in sub:
#         sub.append(i)
#     else:
#         x.append(sub)
#         sub=[i]
# print(x+[sub])



l = list(map(int,input().split()))
x = []
sub = [l[0]]
i = 1
while len(l)!=0:
    if i==len(l):
        print(sub)
        l=x
        i=0
        if len(l)==0:
            break
        sub=[]
        x= []

    if l[i] not in sub:
        sub.append(l[i])
    else:
        x.append(l[i])
    i+=1


    # print(l)

