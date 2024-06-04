#strings
def is_pal(n,r=""):
    if n==-1:
        return r
    return is_pal(n-1,r+s[n])

s = input()
t = is_pal(len(s)-1)
print(s==t)


#integers
def is_pal(t,r=0):
    if t==0:
        return r
    return is_pal(t//10,r*10+(n%10))

n = int(input())
t = is_pal(n)
print(s==t)



