# 1. 입력 받기
# 2. 그래프 만들기 index번째의 연결 노드
# 3. 재귀 방식의 dfs를 통해 바이러스 걸린 컴퓨터 찾기
# 4. dfs에 들어온 노드를 방문 처리하기
# 5. 해당 노드에 연결된 노드를 순회하기
#   이때, 방문하지 않은 노드만 dfs돌리기

def dfs(node):
    global count
    visited[node] = True
    if node != 1:
        count += 1
    for linkedNode in graph[node]:
        if not visited[linkedNode]:
            dfs(linkedNode)

n = int(input())
m = int(input())
graph = []
for _ in range(n+1):
    graph.append([])
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

count = 0
visited = [False] * (n+1)
dfs(1)
print(count)