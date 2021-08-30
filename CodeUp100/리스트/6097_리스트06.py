# 설탕과자 뽑기
w, h = map(int, input().split())
n = int(input())
board = [[0] * h for _ in range(w)]
for i in range(n):
    l, d, x, y = map(int, input().split())
    for j in range(l):
        if d == 0:
            board[x-1][y-1+j] = 1
        else:
            board[x-1+j][y-1] = 1
for i in range(w):
    for j in range(h):
        print(board[i][j], end=' ')
    print()
