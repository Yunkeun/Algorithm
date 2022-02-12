N = int(input())
location = []
for _ in range(N):
    x, y = list(map(int, input().split()))
    location.append([y, x])
location.sort()
for y, x in location:
    print(x,y)