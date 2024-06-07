
#using stack
s = input()
stack = []
p = 0
d = {
    "}":"{",
    "]":"[",
    ")":"("
}
f=1
for i in s:
    print(i)
    if  i in "[({":
        stack.append(i)
    elif stack:
        print(i)
        if stack[-1]==d[i]:
            stack.pop()
        else:
            f=0
            print(p+1)
            break
    else:
        f=0
        print(p+1)
        break
    p+=1

if f:
    print("-1")

