N, M = map(int, input().split())
res = 0
for i in range(N):
    row = list(map(int, input().split()))
    if (res < min(row)):
        res = min(row)
print(res)