s = input().split(",")
st = ""
for d in s:
    i,j=d.split(":")
    l = len(i)
    flag=0
    print(i,j)
    while l!=0:
        if str(l) in j:
            flag=1
            st+=i[l-1]
            break
        l-=1
    if not flag:
        st+="x"
print(st)
