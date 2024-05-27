
f = int(input())
l = int(input())
c= 0

# not optimal solution
for i in range(f,l+1):
    if i%7==0:
        c+=1
print(c)



# optimal solution
l1 = f//7
l2 = l//7
c = l2-l1
print(c)
