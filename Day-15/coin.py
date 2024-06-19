# l = [2,3,5,6]
# n = 11
# m = [[0 for j in range(11)]for i in range(len(l)+1)]
# for i in range(len(m)):
#     m[i][0]=1
# for i in range(1,len(l)):
#     for j in range(n):
#         if j<l[i]:
#             m[i][j]=m[i-1][j]
#         else:
#             if m[i-1][j]==1:
#                 m[i][j]=1
#             elif l[i]==j:
#                 m[i][j]=1
#             else:
#                 s = j-l[i]
#                 m[i][j]=m[i-1][s]
# for i in m:
#     print(i)




# [2,3,5,6] op : 11
#  we have all coins only 1 is that possible to make target
nums = [2,3,5,6]
target = 7


table =[[0]*(target+1) for _ in range(len(nums)+1)]

for i in range(target+1):
    table[0][i] = 0
for i in range(len(nums)+1):
    table[i][0] = 1
for i in range(1,len(nums)+1):
    for j in range(1,target+1):
        table[i][j] = table[i-1][j]
        if j == nums[i-1]:table[i][j] = 1
        elif j>table[i][j]:
            table[i][j] = 1 if (table[i-1][j-nums[i-1]] or table[i-1][j]) else 0
for row in table:
    print(*row)
