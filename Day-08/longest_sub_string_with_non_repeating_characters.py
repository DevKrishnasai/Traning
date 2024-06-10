s = input()
i=0
j = 0
l = []
x = ""
while j<len(s):
    if s[j] not in x:
        x+=s[j]
        j+=1
    else:
        l.append((x,len(x)))
        index = x.index(s[j])
        x=x[index+1:]
        i=s.index(s[j])
    i+=1

print(l)


