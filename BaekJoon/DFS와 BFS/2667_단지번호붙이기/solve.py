# bfs
from collections import deque

n = int(input())
graph = [list(map(int, input())) for _ in range(n)]
# 이동할 방향 정의
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    # 현재 위치 방문 처리
    graph[x][y] = 0
    count = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 공간 벗어나는 경우 continue
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            # 방문하지 않은 위치(1)이라면 방문 처리(0으로) 한 후 queue에 넣어주기
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx, ny))
                count += 1
    return count

result = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            result.append(bfs(i, j))
result.sort()
print(len(result))
for res in result:
    print(res)