s = input()
d = ""
for i in s:
    if i in "aeiouAEIOU":
        d+=i.upper()
    else:
        d+=i.lower()
print(d)

