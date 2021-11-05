N = int(input())
answer = 0

for i in range(1, N):
    decomposition = 0
    for c in str(i):
        decomposition += int(c)
    if decomposition + i == N:
        answer = i
        break
    else:
        if i == N-1:
            answer = 0
            break
print(answer)