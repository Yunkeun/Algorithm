# 정수를 입력 받아 그 수 만큼 숫자를 입력하여 가장 작은 수 출력하기
n = int(input())
num = list(map(int, input().split()))
num.sort()
print(num[0])