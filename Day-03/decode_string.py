
#left rotation
s = input()
k = int(input())
n = len(s)
letters = "abcdefghijklmnopqrstuvwxyz"
k%=26
res =[]
for i in s:
    char = ord(i) - ord("a") - k
    res.append(letters[char])
print("".join(res))


#right rotation
s = input()
k = int(input())
n = len(s)
letters = "abcdefghijklmnopqrstuvwxyz"
res =[]
k%=26
for i in s:
    char = ord(i) - ord("a") + k
    char%=26
    res.append(letters[char])
print("".join(res))



