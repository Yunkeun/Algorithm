# 그래프(n x n) 입력
# 방문 (n x n)입력
# 그래프 순회하며 시작점 찾기
    # 순회하며 좌표가 not visited 이면서 1이면 dfs(i, j)
# 방향 설정 -> 상하좌우 4방향
# dfs 정의 dfs(x, y)
    # x, y가 유효한 값(0~n 사이)인지 확인
    # 해당 좌표 방문 처리
    # 좌표값이 1이면 count += 1
    # 현재 좌표부터 상하좌우 움직이며 not visited면서 1이면 dfs
# 한 단지 내 아파트를 모두 count하면 dfs 탈출 => count를 배열에 추가 및 count 초기화

def dfs(x, y):
    global count
    visited[x][y] = True
    count += 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if graph[nx][ny] == 1 and not visited[nx][ny]:
                dfs(nx, ny)

n = int(input())
graph = []
visited = []
for _ in range(n):
    graph.append(list(map(int, input())))
    visited.append([False]*n)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
count = 0
numInHouseComplexes = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and not visited[i][j]:
            dfs(i, j)
            numInHouseComplexes.append(count)
            count = 0
numInHouseComplexes.sort()
print(len(numInHouseComplexes))
for num in numInHouseComplexes:
    print(num)