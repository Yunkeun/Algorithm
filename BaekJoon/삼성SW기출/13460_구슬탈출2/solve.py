from collections import deque

# board의 크기를 입력받는다.
n, m = map(int, input().split())
# board를 입력 받는다. (n만큼 반복해서 입력 받는다.)
board = [list(input()) for _ in range(n)]
# 방문 여부를 확인할 check 배열을 4차원 배열로 선언한다.
check = [[[[False] * m for _ in range(n)] for _ in range(m)] for _ in range(n)]
# 구슬의 움직임을 표현한다.
dx, dy = (-1, 0, 1, 0), (0, -1, 0, 1)
# 큐를 정의한다.
queue = deque()


def init():
    # red와 blue의 x, y 좌표를 0으로 초기화한다.
    redX, redY, blueX, blueY = [0] * 4
    # board를 탐색하여 R과 B의 좌표를 저장한다.
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'R':
                redX, redY = i, j
            elif board[i][j] == 'B':
                blueX, blueY = i, j
    # 큐에 집어 넣고 방문을 표시한다.
    queue.append((redX, redY, blueX, blueY, 0))
    check[redX][redY][blueX][blueY] = True


# x, y: 현재 좌표
# dx, dy: 이동
def move(x, y, dx, dy, count):
    # 현재 좌표가 O가 아니고 이동할 좌표가 # 이 아니면 이동한다.
    while board[x + dx][y + dy] != '#' and board[x][y] != 'O':
        x += dx
        y += dy
        count += 1
    return x, y, count

def bfs():
    # queue가 빌 때 까지 반복한다.
    while queue:
        # queue에서 pop한 값을 저장한다.
        redX, redY, blueX, blueY, count = queue.popleft()
        if count >= 10:
            break
        # 이동 가지수가 4개이므로 4번 반복한다.
        for i in range(4):
            # red와 blue가 따로 이동하므로 각각 move
            # count에 0을 넣어 이동가능하면 1, 아니라면 0 리턴
            newRedX, newRedY, redCount = move(redX, redY, dx[i], dy[i], 0)
            newBlueX, newBlueY, blueCount = move(blueX, blueY, dx[i], dy[i], 0)
            # blue가 O 이라면 건너뛰기
            if board[newBlueX][newBlueY] == 'O':
                continue
            # red가 O 이라면 개수 출력 후 종료
            if board[newRedX][newRedY] == 'O':
                print(count + 1)
                return
            # red와 blue 위치가 같을 때 red가 이동가능하다면 red 이동 전으로, 아니라면 blue 이동 전으로
            if newRedX == newBlueX and newRedY == newBlueY:
                if redCount > blueCount:
                    newRedX, newRedY = newRedX - dx[i], newRedY - dy[i]
                else:
                    newBlueX, newBlueY = newBlueX - dx[i], newBlueY - dy[i]
            # 현재 위치가 방문하지 않은 장소라면 방문 표시 후 큐에 집어 넣는다.
            if not check[newRedX][newRedY][newBlueX][newBlueY]:
                check[newRedX][newRedY][newBlueX][newBlueY] = True
                queue.append((newRedX, newRedY, newBlueX, newBlueY, count + 1))
    print(-1)


init()
bfs()
