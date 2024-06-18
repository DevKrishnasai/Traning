#without blocks
n = 4
m = 3
l = []
z = 0

for i in range(m):
    x = []
    for j in range(n):
        x.append(z)
        z += 1
    l.append(x)

def find_paths(i, j, lx, paths, visited):
    if i == m-1 and j == n-1:
        lx.append(l[i][j])
        paths.append(lx.copy())
        return
    if i >= m or j >= n:
        return

    lx.append(l[i][j])
    visited[i][j] = True

    if i > 0 and not visited[i-1][j]:
        find_paths(i-1, j, lx, paths, visited)
    if i < m-1 and not visited[i+1][j]:
        find_paths(i+1, j, lx, paths, visited)
    if j > 0 and not visited[i][j-1]:
        find_paths(i, j-1, lx, paths, visited)
    if j < n-1 and not visited[i][j+1]:
        find_paths(i, j+1, lx, paths, visited)

    lx.pop()
    visited[i][j] = False


paths = []
visited = [[False] * n for _ in range(m)]
find_paths(0, 0, [], paths,visited)

for path in paths:
    print(path)


print(*l)
print(len(paths))






#if there is any block in between
n = 4
m = 3
l = []
z = 0

target = (1,3)

for i in range(m):
    x = []
    for j in range(n):
        x.append(z)
        z += 1
    l.append(x)

def find_paths(i, j, lx, paths, visited):
    if i==target[0] and j==target[-1]:
        return
    if i == m-1 and j == n-1:
        lx.append(l[i][j])
        paths.append(lx.copy())
        return
    if i >= m or j >= n:
        return
    lx.append(l[i][j])
    visited[i][j] = True

    if i > 0 and not visited[i-1][j]:
        find_paths(i-1, j, lx, paths, visited)
    if i < m-1 and not visited[i+1][j]:
        find_paths(i+1, j, lx, paths, visited)
    if j > 0 and not visited[i][j-1]:
        find_paths(i, j-1, lx, paths, visited)
    if j < n-1 and not visited[i][j+1]:
        find_paths(i, j+1, lx, paths, visited)

    lx.pop()
    visited[i][j] = False


paths = []
visited = [[False] * n for _ in range(m)]
find_paths(0, 0, [], paths,visited)

for path in paths:
    print(path)


print(*l)
print(len(paths))


