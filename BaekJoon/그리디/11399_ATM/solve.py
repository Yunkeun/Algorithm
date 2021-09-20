N = int(input())
P = list(map(int, input().split(' ')))
P.sort()
res = 0
for i in range(1, N):
    P[i] += P[i-1]
res = sum(P)
print(res)
