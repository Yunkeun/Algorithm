from collections import deque

test_number = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
result = []

def init_graph():
    graph = [[0] * m for _ in range(n)]
    for _ in range(cabbage_num):
        x, y = map(int, input().split())
        graph[y][x] = 1
    return graph

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx,ny))
        
for _ in range(test_number):
    m, n, cabbage_num = map(int, input().split())
    graph = init_graph()
    count = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                bfs(i, j)
                graph[i][j] = 0
                count += 1
    result.append(count)
for res in result:
    print(res)