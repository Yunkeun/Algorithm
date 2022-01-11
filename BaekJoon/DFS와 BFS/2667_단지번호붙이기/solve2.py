# dfs

n = int(input())
graph = [list(map(int, input())) for _ in range(n)]
# 이동할 방향 정하기 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    # 공간을 벗어난 경우 return
    if x < 0 or x >= n or y < 0 or y >= n:
        return False
    if graph[x][y] == 1:
        global count
        count += 1
        # 현재 위치 방문 처리
        graph[x][y] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx, ny)
        return True
    return False

count = 0
result = []

for i in range(n):
    for j in range(n):
        if dfs(i, j):
            result.append(count)
            count = 0
result.sort()
print(len(result))
for res in result:
    print(res)