N = int(input())
location = []
for _ in range(N):
    location.append(list(map(int, input().split())))
location.sort()
for i in range(N):
    print(location[i][0], location[i][1])