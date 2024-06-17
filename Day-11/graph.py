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

def bfs(start):
    visited = []
    q = [start]
    while q:
        for i in d[q[0]]:
            if i not in q and i not in visited:
                q.append(i)
        visited.append(q.pop(0))
    print(visited)



def recusiveBFS(start):
    visited = []
    q = [start]
    def res():
        if not q:
            return
        for i in d[q[0]]:
            if i not in q and i not in visited:
                q.append(i)
        visited.append(q.pop(0))
        res()
    res()
    print(visited)

def dijkstra(start, d):
    dist = {5:float('inf'),7:float('inf'),4:float('inf'),8:float('inf'),3:float('inf'),2:float('inf')}
    q = [start]
    v = set()
    dist[start]=0
    min_d=start
    while q:
        print(q)
        m = float('inf')
        for i in q:
            if dist[i]<m:
                m=dist[i]
                min_d=i
        for i in d[min_d]:
            if i not in v:
                q.append(i[0])
                if dist[i[0]]>i[1]+dist[min_d]:
                    dist[i[0]]=i[1]+dist[min_d]
        v.append(min_d)
        q.remove(min_d)
    print(v)










# d = {5:[7,3],7:[5,4,3],4:[7,8,2],8:[3,4,2],3:[5,7,8],2:[4,8]}
d = {5:[(7,1),(3,2)],7:[(5,1),(4,5),(3,3)],4:[(7,5),(8,2),(2,2)],8:[(3,2),(4,2),(2,3)],3:[(5,2),(7,3),(8,2)],2:[(4,2),(8,3)]}
# printNodes(5)
# printAllPathsFromStartToEnd(5,2)
# printAllPathsFromStartToEndWithCost(5,2)
# PrintMinCostPath(5,2)
# PrintMaxCostPath(5,2)
# bfs(5)

dijkstra(5,d)

# g = {
#     0 :[(0,0),(1,1),(2,2)],
#     1:[(0,1),(2,4),(3,6)],
#     2:[(4,9),(1,4),(0,2)],
#     3:[(1,6),(4,1),(5,4)],
#     4:[(3,1) ,(5,4),(2,9)],
#     5:[(4,4),(3,4)]
# }

# dist = [float("inf")]*6

# dist[0] =0

# import heapq
# heap = []
# heapq.heapify(heap)
# visited = set()
# visited.add(0)
# heapq.heappush(heap,(0,0))
# while heap:
#     node,cost = heapq.heappop(heap)
#     for neigh,cost in g[node]:
#         dist[neigh] = min(dist[neigh],cost + dist[node])
#         if neigh not in visited:
#             visited.add(neigh)
#             heapq.heappush(heap,(neigh,dist[neigh]))
# print(dist)
