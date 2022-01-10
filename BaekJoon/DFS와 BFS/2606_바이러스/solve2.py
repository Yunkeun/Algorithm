N = int(input())
M = int(input())

graph = [[0] * (N + 1) for _ in range(N + 1)]
count = 0
for _ in range(M):
    m1, m2 = map(int, input().split())
    graph[m1][m2] = graph[m2][m1] = 1

def dfs(started_v, visited=[]):
    global count
    visited.append(started_v)

    for w in range(len(graph[started_v])):
        if graph[started_v][w] == 1 and w not in visited:
            count += 1
            dfs(w, visited)

dfs(1)
print(count)