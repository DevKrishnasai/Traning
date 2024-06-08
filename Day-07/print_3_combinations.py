l = [1,2,3,4,5]
k = 3
# le = len(l)

# for i in range(le-2):
#     for j in range(i+1,le-1):
#         for k in range(j+1,le):
#             print(l[i],l[j],l[k])
# print("--------------")
# x= []
# def recc(i,j,k):
#     if i==len(l)-2 or j==len(l)-1 or k==len(l):
#         return
#     # x.append((l[i],l[j],l[k]))
#     print(l[i],l[j],l[k])
#     recc(i,j,k+1)
#     recc(i,j+1,j+2)
#     recc(i+1,i+2,i+3)
#     # return

# # recc(0,1,2)
# # print(x)



def recc(x,i):
    if len(x)==k:
        print(x)
        return
    for j in range(i,len(l)):
        print("before",j,i,x)
        recc(x+[l[j]],j+1)
        print("after",j,i,x)
    return
recc([],0)
