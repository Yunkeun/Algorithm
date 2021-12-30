# 왕실의 나이트
row = [1, 2, 3, 4, 5, 6, 7, 8]
col = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
currentPosition = input()
current_row = int(currentPosition[1])
current_col = ord(currentPosition[0])
count = 0
movements = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]
for move in movements:
    if (current_row + move[0] in row and chr(current_col + move[1]) in col):
        count += 1
print(count)