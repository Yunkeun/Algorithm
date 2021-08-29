# 정수를 입력 받아 그 수 만큼 흰 돌의 좌표를 입력하여 19*19 바둑판 출력하기 (흰 돌이 있는 곳: 1, 아닌 곳: 0)
n = int(input())
board = list()
for i in range(n):
    board.append(list(map(int, input().split())))
#print(board)
board_all = [[0] * 19 for _ in range(19)]
for i in range(1, 20):
    for j in range(1, 20):
        if [i, j] in board:
            print(1, end=' ') 
        else:
            print(0, end=' ')
    print()