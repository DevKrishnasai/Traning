def printNodes(start):
    l = []
    def printNode(node):
        l.append(node)
        for i in d[node]:
            if i not in l:
                printNode(i)
    printNode(start)
    return l

def printAllPathsFromStartToEnd(start,end):
    def printPath(val,l):
        l.append(val)
        if val==end:
            print(l)
            l.pop()
            return
        for i in d[val]:
            if i[0] not in l:
                printPath(i[0],l)
        l.pop()
    printPath(start,[])

# def printAllPathsFromStartToEndWithCost(start,end):
#     def printPath(val,l,c=0):
#         l.append(val)
#         if val==end:
#             print(l,c)
#             l.pop()
#             return
#         for i in d[val]:
#             if i[0] not in l:
#                 c+=i[1]
#                 printPath(i[0],l,c)
#                 c-=i[1]

#         l.pop()
#     printPath(start,[])

def PrintMaxCostPath(start,end):
    def PrintMaxCostWithPath(val,l,c=0,mx=0,x=[]):
        l.append(val)
        if val==end:
            l.pop()
            if mx<c:
                mx=c
                x = l.copy()
            return mx,x
        for i in d[val]:
            if i[0] not in l:
                c+=i[1]
                mx,x=PrintMaxCostWithPath(i[0],l,c,mx,x)
                c-=i[1]
        l.pop()
        return (mx,x)

    print(PrintMaxCostWithPath(start,[]))

def PrintMinCostPath(start,end):
    def PrintMinCostWithPath(val,l,c=0,mi=99999,x=[]):
        l.append(val)
        if val==end:
            l.pop()
            if mi>c:
                mi=c
                x = l.copy()
            return mi,x
        for i in d[val]:
            if i[0] not in l:
                c+=i[1]
                mi,x=PrintMinCostWithPath(i[0],l,c,mi,x)
                c-=i[1]
        l.pop()
        return (mi,x)
    print(PrintMinCostWithPath(start,[]))


# d = {5:[7,3],7:{5,4,3},4:[7,8,2],8:[3,4,2],3:[5,7,8],2:[4,8]}
d = {5:[(7,1),(3,2)],7:[(5,1),(4,5),(3,3)],4:[(7,5),(8,2),(2,2)],8:[(3,2),(4,2),(2,3)],3:[(5,2),(7,3),(8,2)],2:[(4,2),(8,3)]}
# printNodes(5)
# printAllPathsFromStartToEnd(5,2)
# printAllPathsFromStartToEndWithCost(5,2)
PrintMinCostPath(5,2)
PrintMaxCostPath(5,2)
