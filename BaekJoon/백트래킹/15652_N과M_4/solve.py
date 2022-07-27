def dfs():
    if len(s) == m:
        print(' '.join(map(str, s)))
        return
    for i in range(1, n+1):
        if s and max(s) > i:
            continue
        visited[i] = True
        s.append(i)
        dfs()
        visited[i] = False
        s.pop()

n, m = map(int, input().split())
s = []
visited = [False] * (n+1)
dfs()