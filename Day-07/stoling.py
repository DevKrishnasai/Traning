# method 1
l = [13,9,4,10,5,7]
x = []
def recurr(i,s):
    if i>=len(l):
        x.append(s)
        print("sum: ",s)
        return
    print("before",i,s)
    recurr(i+2,s+l[i])
    print("------------------")
    recurr(i+1,s)
    print("after",i,s)
recurr(0,0)
print(max(x))

# method 2
l = [13,9,4]
def recurr2(s):
    if len(s)==0:
        return 0
    if len(s)==1:
        return s[0]
    if len(s)==2:
        return max(s)
    even = s[0]+recurr2(s[2:])
    odd = s[1]+recurr2(s[3:])
    return max(even,odd)
print(recurr2(l))

l = [13,9,4]

dp = [0]*len()
