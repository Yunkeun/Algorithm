n = int(input())

listA = list(map(int, input().split()))
listB = list(map(int, input().split()))

S = 0
for i in range(n):
    minA = min(listA)
    maxB = max(listB)
    S += minA * maxB
    listA.pop(listA.index(minA))
    listB.pop(listB.index(maxB))

print(S)