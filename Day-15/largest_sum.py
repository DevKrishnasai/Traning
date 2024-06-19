# s1 = input()
# s2 = input()
s1,s2="tu5g2k1h8","g5g8gd6h3"
s=set()
for i in s1:
    if i.isdigit():
        s.add(i)

for i in s2:
    if i.isdigit():
        s.add(i)

s = sorted(list(s))[::-1]
for i in range(len(s)-1,-1,-1):
    if s[i]%2==0:
        s.append(s.pop(i))
        break
if s[-1]%2:
    print(-1)
else:
    print("".join(s))
