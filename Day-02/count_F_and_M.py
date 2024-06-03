s = input()

l = []

for i in s:
    if i == "F":
        l.append(i)
    else:
        l.pop()
print(l)
