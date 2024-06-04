s = input()
i = 0
j = 0
l = []


while j<len(s)-1:
    if ord(s[j])==ord(s[j+1])-1:
        j+=1
    else:
        l.append((j-i+1,s[i:j+1]))
        j+=1
        i=j
l.append((j-i+1,s[i:j+1]))
print(l)
