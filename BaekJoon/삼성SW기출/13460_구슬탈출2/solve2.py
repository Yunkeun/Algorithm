from collections import deque

n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]

check = [[[[False] * m for _ in range(n)] for _ in range(m)] for _ in range(n)]
dx, dy = (1, 0, -1, 0), (0, 1, 0, -1)
q = deque()

def init():
    redX, redY, blueX, blueY = [0] * 4
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'R':
                redX, redY = i, j
            elif board[i][j] == 'B':
                blueX, blueY = i, j
    q.append((redX, redY, blueX, blueY, 0))
    check[redX][redY][blueX][blueY] = True

def move(x, y, dx, dy, count):
    while(board[x+dx][y+dy] != '#' and board[x][y] != 'O'):
        x += dx
        y += dy
        count += 1
    return x, y, count

def bfs():
    while (q):
        redX, redY, blueX, blueY, count = q.popleft()
        if count >= 10:
            break
        for i in range(4):
            newRedX, newRedY, redCount = move(redX, redY, dx[i], dy[i], 0)
            newBlueX, newBlueY, blueCount = move(blueX, blueY, dx[i], dy[i], 0)
            if board[newBlueX][newBlueY] == 'O':
                continue
            if board[newRedX][newRedY] == 'O':
                print(count + 1)
                return
            if newRedX == newBlueX and newRedY == newBlueY:
                if redCount > blueCount:
                    newRedX -= dx[i]
                    newRedY -= dy[i]
                else:
                    newBlueX -= dx[i]
                    newBlueY -= dy[i]
            if not check[newRedX][newRedY][newBlueX][newBlueY]:
                check[newRedX][newRedY][newBlueX][newBlueY] = True
                q.append((newRedX, newRedY, newBlueX, newBlueY, count+1))
    print(-1)

init()
bfs()