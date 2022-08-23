from collections import deque

def bfs(x, y, count):
    q = deque()
    q.append([x, y, count])
    visited[x][y] = True
    maxCount = 0
    while q:
        a, b, currentCount = q.popleft()
        if currentCount > maxCount:
            maxCount = currentCount
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 'L' and not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append([nx, ny, currentCount+1])
    return maxCount

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(input()))
count = 0
dx = [1,-1,0,0]
dy = [0,0,1,-1]
for i in range(n):
    for j in range(m):
        # 위,아래에 L이 있다면, 끝점이 아님 -> continue
        if i > 0 and i+1 < n:
            if graph[i-1][j] == 'L' and graph[i+1][j] == 'L':
                continue
        # 좌,우에 L이 있다면, 끝점이 아님 -> continue
        if j > 0 and j+1 < m:
            if graph[i][j-1] == 'L' and graph[i][j+1] == 'L':
                continue
        if graph[i][j] == 'L':
            visited = []
            for _ in range(n):
                visited.append([False] * m)
            cur = bfs(i, j,0)
            count = max(count, cur)
print(count)