# 숫자 뒤집기
d = list(list(map(int, input().split())) for _ in range(19))
n = int(input())
standard = list()
for i in range(n):
    standard.append(list(map(int, input().split())))
for i in range(1, 20):
    for j in standard:
        if j[0] == i:
            for k in range(1, 20):
                if d[i-1][k-1] == 1:
                    d[i-1][k-1] = 0
                elif d[i-1][k-1] == 0:
                    d[i-1][k-1] = 1
        if j[1] == i:
            for k in range(1, 20):
                if d[k-1][i-1] == 1:
                    d[k-1][i-1] = 0
                elif d[k-1][i-1] == 0:
                    d[k-1][i-1] = 1
for i in range(19):
    for j in range(19):
        print(d[i][j], end=' ')
    print()