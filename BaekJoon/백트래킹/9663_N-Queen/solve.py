def isPromising(x):
    for i in range(x):
        if row[x] == row[i] or abs(x-i) == abs(row[x] - row[i]): # 같은 행에 있거나
            return False
    return True

def nQueens(x):
    global ans
    if x == n:
        ans += 1
        return
    for i in range(n):
        row[x] = i
        if isPromising(x):
            nQueens(x+1)

n = int(input())
row = [0] * n
ans = 0
nQueens(0)
print(ans)