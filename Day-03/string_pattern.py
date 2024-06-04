n = int(input())

tot = n*2+1
c = 97
l = "abcdefghijklmnopqrstuvwxyz"

for i in range(1,n+1):
    t = tot//2
    print("_ "*(t),end=" ")

    s = l[:i]
    f = list(s[::-1]+s[1:])
    print(" ".join(f),end=" ")

    print("_ "*(t),end=" ")
    print()

    tot-=2
    c+=1


