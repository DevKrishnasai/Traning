l = input().split()
o,e,f=0,0,0
for i in l:
    if "." in i:
        f+=float(i)
    elif int(i)%2!=0:
        o+=int(i)
    else:
        e+=int(i)
print(o,e,f)
