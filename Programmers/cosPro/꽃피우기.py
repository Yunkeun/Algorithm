# 다음과 같이 import를 사용할 수 있습니다.
# import math

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def solution(garden):
    # 여기에 코드를 작성해주세요
    # loop 1 and !visited 찾기
    # 1 찾으면 상하좌우 0이면 1로 변경 후 break (방문 체크)
    answer = 0
    visited = [[False] * len(garden) for _ in range(len(garden))]

    while not check(garden):
        answer = search(garden, visited, answer)
    return answer

def search(garden, visited, answer):
    answer += 1
    tmpVisited = []
    for i in range(len(garden)):
        for j in range(len(garden)):
            if garden[i][j] == 1 and not visited[i][j] and [i,j] not in tmpVisited:
                visited[i][j] = True
                for v in range(4):
                    nx = i + dx[v]
                    ny = j + dy[v]
                    if 0 <= nx < len(garden) and 0 <= ny < len(garden):
                        if garden[nx][ny] == 0:
                            garden[nx][ny] = 1
                            tmpVisited.append([nx, ny])
    return answer



    
def check(garden):
    for row in garden:
        for v in row:
            if v == 0:
                return False
    return True
    

# 아래는 테스트케이스 출력을 해보기 위한 코드입니다.
garden1 = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
ret1 = solution(garden1)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret1, "입니다.")

garden2 = [[1, 1], [1, 1]]
ret2 = solution(garden2)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret2, "입니다.")

# 아래는 테스트케이스 출력을 해보기 위한 코드입니다.
garden3 = [[0, 1, 0], [0, 1, 0], [0, 0, 0]]
ret3 = solution(garden3)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret3, "입니다.")