N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())
count = 0

for i in range(N):
    if A[i] > 0:
        A[i] -= B
        count += 1
    if A[i] > 0:    
        count += A[i] // C
        if A[i] % C > 0:
            count += 1

print(count)