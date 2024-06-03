# method 1 with strings
# def getSum(a):
#     s=0
#     for i in a:
#         s+=int(i)
#     return str(s)


# n = input()
# s = getSum(n)
# while True:
#     if len(s)>1:
#         s = getSum(s)
#     else:
#         if s in "2357":
#             # print(s)
#             break
#         n = int(n)+1
#         s= n
# print(n)


#method 2 with integers
# def getSum(a):
#     s=0
#     while a>0:
#         r = a%10
#         s+=r
#         a = a//10
#     return s


# n = int(input())
# s = getSum(n)
# while True:
#     if s>9:
#         s = getSum(s)
#     else:
#         if s in [2,3,5,7]:
#             # print(s)
#             break
#         n = n+1
#         s= n
# print(n)




