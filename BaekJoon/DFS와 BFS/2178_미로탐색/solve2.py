from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]

# directions
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(a, b):
    queue = deque()
    queue.append((a, b))

    while queue:
        x, y = queue.popleft()
        for i in range(len(dx)):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    return graph[n-1][m-1]
    
print(bfs(0, 0))
