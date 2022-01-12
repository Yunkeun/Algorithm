from collections import deque

m, n = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]
queue = deque()
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
result = 0

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            queue.append((i, j))

def bfs():
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

bfs()
for row in graph:
    for x in row:
        if x == 0:
            print(-1)
            exit(0)
    result = max(result, max(row))
print(result - 1)