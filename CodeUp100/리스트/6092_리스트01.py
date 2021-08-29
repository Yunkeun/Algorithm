# 정수를 입력 받아 그 수 만큼 번호(1~23)를 입력하여 입력된 수 횟수 세어 출력하기
n = int(input())
num = input().split(' ')
res = [0 for _ in range(24)]
for i in range(n):
    res[int(num[i])] += 1
for i in range(1, 24):
    print(res[i], end=' ')