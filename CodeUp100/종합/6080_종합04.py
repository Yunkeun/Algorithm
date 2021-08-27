# 1부터 n까지, 1부터 m까지 두 개의 주사위의 경우의 수 모두 출력하기
n, m = map(int, input().split(' '))
for i in range(1, n+1):
    for j in range(1, m+1):
        print(i, j)