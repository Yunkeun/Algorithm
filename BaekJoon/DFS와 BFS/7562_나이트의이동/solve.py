from collections import deque

dx = [2, 1, -1, -2, -2, -1, 1, 2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]

def bfs(a, b, c, d):
    queue = deque()
    queue.append((a, b))

    while queue:
        x, y = queue.popleft()
        if x == c and y == d:
            print(graph[x][y] - 1)
            return True

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= l or ny < 0 or ny >= l:
                continue
            if graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

    return False

n = int(input())
for i in range(n):
    l = int(input())
    graph = [[0] * l for _ in range(l)]
    a, b = map(int, input().split())
    c, d = map(int, input().split())
    graph[a][b] = 1
    bfs(a, b, c, d)