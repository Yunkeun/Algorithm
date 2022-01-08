N, M = map(int, input().split())
board = []
count = []
for i in range(N):
    board.append(list(input()))

def count_painting(chess):
    count = 0
    first_color = chess[0][0]
    for r in range(0, 8):
        for c in range(0, 8):
            if r == 0 and c == 0:
                continue
            if first_color == 'W':
                if r % 2 == 0:
                    if c % 2 == 1 and chess[r][c] == 'W':
                        count += 1
                    elif c % 2 == 0 and chess[r][c] == 'B':
                        count += 1
                elif r % 2 == 1:
                    if c % 2 == 1 and chess[r][c] == 'B':
                        count += 1
                    elif c % 2 == 0 and chess[r][c] == 'W':
                        count += 1
            else:
                if r % 2 == 0:
                    if c % 2 == 1 and chess[r][c] == 'B':
                        count += 1
                    elif c % 2 == 0 and chess[r][c] == 'W':
                        count += 1
                elif r % 2 == 1:
                    if c % 2 == 1 and chess[r][c] == 'W':
                        count += 1
                    elif c % 2 == 0 and chess[r][c] == 'B':
                        count += 1
    return count

# 시작 찾기
for i in range(0, N-7):
    for j in range(0, M-7):
        chess = []
        for k in range(i, 8+i):
            chess_row = []
            for l in range(j, 8+j):
                chess_row.append(board[k][l])
            chess.append(chess_row)
        # 다시 칠해야 하는 정사각형 개수 구하기
        count.append(count_painting(chess))
        # 제일 앞 자리를 바꿨을 때 다시 칠해야 하는 정사각형 개수 구하기
        if chess[0][0] == 'W':
            chess[0][0] = 'B'
        else:
            chess[0][0] = 'W'
        count.append(count_painting(chess))
        count[-1] += 1
print(min(count))
