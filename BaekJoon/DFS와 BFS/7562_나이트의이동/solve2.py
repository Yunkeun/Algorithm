from collections import deque

n = int(input())

# directions
dx = [2, 2, 1, 1, -1, -1, -2, -2]
dy = [1, -1, 2, -2, 2, -2, 1, -1]

# bfs
def bfs(a, b, mx, my):
    queue = deque()
    queue.append((a, b))

    while queue:
        x, y = queue.popleft()
        if x == mx and y == my:
            return graph[x][y]
        for i in range(len(dx)):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < length and 0 <= ny < length and graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    return graph[nx][ny]

for i in range(n):
    length = int(input())
    graph = [[0] * length for _ in range(length)]
    currentX, currentY = map(int, input().split())
    toMoveX, toMoveY = map(int, input().split())
    print(bfs(currentX, currentY, toMoveX, toMoveY))
