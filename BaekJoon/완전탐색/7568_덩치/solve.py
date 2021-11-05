N = int(input())
body_info = []
for i in range(N):
    w, h = map(int, input().split(' '))
    body_info.append((w, h))

for i in body_info:
    rank = 1
    for j in body_info:
        if (i[0] < j[0] and i[1] < j[1]):
            rank += 1
    print(rank, end=" ")