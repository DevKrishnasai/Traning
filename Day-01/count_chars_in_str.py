s = input()
l = set(list(s))

# method 1 (PARTIAL)
# for i in l:
#     j = 0
#     c=0
#     while j<len(s):
#         if s[j]==i:
#             c+=1
#         j+=1
#     print(i,c)

# method 2
# i = 0
# j = 0
# c=0
# while  j<len(s):
#     if s[i]==s[j]:
#         c+=1
#         j+=1
#     else:
#         print(s[i],c)
#         c=0
#         i=j
# print(s[i],c)

