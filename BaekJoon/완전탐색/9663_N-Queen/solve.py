# 시간초과
def check(x):
    for i in range(x):
        # 열이 같은 조건, 대각선 조건
        if col[x] == col[i] or abs(col[x] - col[i]) == x - i: # 열이 같은 조건
            return False
    return True

def dfs(x):
    global count
    if x == N:
        count += 1
        return
    for i in range(N):
        col[x] = i # x행 i열
        if check(x):
            dfs(x + 1)
N = int(input())
col = [0] * N
count = 0
dfs(0)
print(count)