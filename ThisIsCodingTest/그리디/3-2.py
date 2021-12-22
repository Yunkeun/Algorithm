N, M, K = map(int, input().split())
numbers = list(map(int, input().split()))
sum = 0
numbers.sort(reverse=True)
while M > 0:
    for i in range(K):
        M -= 1
        max = numbers[0]
        sum += max
        if (M == 0):
            break
    if (M == 0):
        break
    M -= 1
    max = numbers[1]
    sum += max
print(sum)
