def fun(start):
    x = []
    for i in range(start,len(l)-2):
        # sub = sorted([l[i],l[i+1],l[i+2]])
        mi = min(l[i],l[i+1],l[i+2])
        mx = min(l[i],l[i+1],l[i+2])
        m = sum([l[i],l[i+1],l[i+2]])-(mi+mx)
        l[i]=mi
        l[i+1]=m
        l[i+2]=mx

l = list(map(int,input().split()))

# for i in range(len(l)-2):
#     fun(i)
fun(0)
print(l)








