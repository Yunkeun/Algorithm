# try again!
from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs():
    queue = deque()
    queue.append((0, 0, 1))
    visit = [[[0] * 2 for _ in range(m)] for _ in range(n)]
    # In [x][y][z], if z == 1 : can crack the wall, if z == 0 : already cracked the wall 
    visit[0][0][1] = 1
    while queue:
        x, y, z = queue.popleft()
        if x == n - 1 and y == m - 1:
            return visit[x][y][z]
        for i in range(len(dx)):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 1 and z == 1:
                    # crack
                    visit[nx][ny][0] = visit[x][y][1] + 1
                    queue.append((nx, ny, 0))
                elif graph[nx][ny] == 0 and visit[nx][ny][z] == 0:
                    visit[nx][ny][z] = visit[x][y][z] + 1
                    queue.append((nx, ny, z))
    return -1
print(bfs())
