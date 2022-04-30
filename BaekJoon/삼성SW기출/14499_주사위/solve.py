n, m, x, y, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
moves = list(map(int, input().split()))

dice = [0 for _ in range(6)]

dx, dy = [0, 0, -1, 1], [1, -1, 0, 0]

for move in moves:
    way = move - 1
    nx = x + dx[way]
    ny = y + dy[way]
    if not 0 <= nx < n or not 0 <= ny < m:
        continue
    if way == 0:
        dice[0], dice[2], dice[3], dice[5] = dice[3], dice[0], dice[5], dice[2]
    elif way == 1:
        dice[0], dice[2], dice[3], dice[5] = dice[2], dice[5], dice[0], dice[3]
    elif way == 2:
        dice[0], dice[1], dice[4], dice[5] = dice[4], dice[0], dice[5], dice[1]
    elif way == 3:
        dice[0], dice[1], dice[4], dice[5] = dice[1], dice[5], dice[0], dice[4]
    
    if graph[nx][ny] == 0:
        graph[nx][ny] = dice[5]
    else:
        dice[5] = graph[nx][ny]
        graph[nx][ny] = 0
    
    x, y = nx, ny
    print(dice[0])