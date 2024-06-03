# Method - 1
s = input()

i= len(s) -1
c = 0
s1 = ""
while i>=0:
    if s[i]=="*":
        c+=1
    else:
        if c==0:
            s1+=s[i]
        else:
            c-=1
    i-=1
print(s1[::-1])


# Method - 2 using stack
s = input()

stack = []

for i in s:
    if stack and i=="*":
        stack.pop()
    else:
        stack.append(i)
print(stack)
