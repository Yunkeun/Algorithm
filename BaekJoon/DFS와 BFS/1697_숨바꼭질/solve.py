from collections import deque

n, k = map(int, input().split())
max_size = 100000
graph = [0] * (max_size+1)

def bfs():
    queue = deque()
    queue.append(n)
    while queue:
        x = queue.popleft()
        if x == k:
            print(graph[x])
            break
        for nx in [x-1, x+1, x*2]:
            if 0 <= nx <= max_size and graph[nx] == 0:
                graph[nx] = graph[x] + 1
                queue.append(nx)

bfs()