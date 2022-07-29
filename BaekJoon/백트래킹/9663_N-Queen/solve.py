def isPromising(x):
    for i in range(x):
        if row[i] == row[x] or abs(x-i) == abs(row[x] - row[i]):
            return False
    return True

def nQueens(x):
    global answer
    if n == x:
        answer += 1
        return
    for i in range(n):
        if visited[i]:
            continue
        row[x] = i
        if isPromising(x):
            visited[i] = True
            nQueens(x+1)
            visited[i] = False

n = int(input())
row = [0] * n
visited = [False] * n
answer = 0
nQueens(0)
print(answer)