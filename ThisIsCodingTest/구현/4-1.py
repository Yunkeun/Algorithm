# 상하좌우
def is_blocked(row, col, move):
    if (row == 1 and move == "U"):
        return True
    if (row == N and move == "D"):
        return True
    if (col == 1 and move == "L"):
        return True
    if (col == N and move == "R"):
        return True
    return False

N = int(input())
moving_planner = input().split()
row = 1
col = 1
for move in moving_planner:
    if (is_blocked(row, col, move)):
        continue
    if (move == "U"):
        row -= 1
    if (move == "D"):
        row += 1
    if (move == "L"):
        col -= 1
    if (move == "R"):
        col += 1
print(row, col)
