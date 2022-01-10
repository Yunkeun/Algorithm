from collections import deque

N = int(input())
M = int(input())

graph = [[0] * (N + 1) for _ in range(N + 1)]
count = 0

for _ in range(M):
    m1, m2 = map(int, input().split())
    graph[m1][m2] = graph[m2][m1] = 1

def bfs(started_v):
    global count
    discovered = [started_v]
    queue = deque()
    queue.append(started_v)
    while queue:
        v = queue.popleft()
        for w in range(len(graph[started_v])):
            if graph[v][w] == 1 and w not in discovered:
                discovered.append(w)
                queue.append(w)
                count += 1

bfs(1)
print(count)