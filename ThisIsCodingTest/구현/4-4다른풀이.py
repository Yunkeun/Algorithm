# 게임 개발

# map 사이즈를 공백으로 구분하여 입력 받기
n, m = map(int, input().split())

# 방문한 위치 맵 0으로 초기화
visit = [[0] * m for _ in range(n)]

# 현재 캐릭터의 X좌표, Y좌표, 방향 입력 받기
x, y, direction = map(int, input().split())

# 현재 좌표 방문
visit[x][y] = 1

# 전체 맵 정보 입력받기
wholeMap = []
for i in range(n):
    wholeMap.append(list(map(int, input().split())))

# 북, 동, 남, 서 방향 정의
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 왼쪽으로 회전하는 함수 정의
def turnLeft():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

# 시뮬레이션 시작
count = 1
turnTime = 0
while True:
    # 왼쪽으로 회전
    turnLeft()
    nx = x + dx[direction]
    ny = y + dy[direction]
    
    # 회전한 이후 정면에 가보지 않은 칸이 존재하는 경우 이동한다.
    if visit[nx][ny] == 0 and wholeMap[nx][ny] == 0:
        visit[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turnTime = 0
        continue
    # 회전한 이후 정면에 가보지 않은 칸이 없거나 바다인 경우 회전한다.
    else:
        turnTime += 1
    # 네 방향 모두 갈 수 없는 경우
    if turnTime == 4:
        nx = x - dx[direction]
        ny = y = dy[direction]
        # 뒤로 갈 수 있다면 이동한다.
        if wholeMap[nx][ny] == 0:
            x = nx
            y = ny
        # 뒤가 바다일 경우 종료한다.
        else:
            break
        turnTime = 0
print(count)