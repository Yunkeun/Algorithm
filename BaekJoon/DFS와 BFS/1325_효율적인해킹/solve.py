from collections import deque

def bfs(x, count):
    q = deque()
    q.append(x)
    visited[x] = True
    while q:
        x = q.popleft()
        for v in graph[x]:
            if not visited[v]:
                visited[v] = True
                q.append(v)
                count += 1
    return count

# n: 컴퓨터 개수, m: 신뢰 관계 개수
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)

maxCountIndexes = []

maxValue = 0
for i in range(1, n+1):
    visited = [False] * (n+1)
    count = bfs(i, 0)
    if count > maxValue:
        maxValue = count
        maxCountIndexes.clear()
        maxCountIndexes.append(i)
    elif count == maxValue:
        maxCountIndexes.append(i)

for v in maxCountIndexes:
    print(v, end=' ')