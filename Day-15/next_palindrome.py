s = input()
if  len(s)%2:
    l = (len(s)//2) + 1
    r = s[:l]
    print(r)
    r+=s[l+1:-1:-1]
    print(r)
else:
    l = len(s)//2
    r = s[:l]
    r+=r[::-1]
    if int(s)<int(r):
        print(r)
    else:
        x = str(int(s[:l])+1)
        x+=x[::-1]
        print(x)


