# 정수 두 개를 입력 받아 두 정수 모두 False라면 True, 아니라면 False 출력하기
n1, n2 = map(int, input().split(' '))
n1 = bool(n1)
n2 = bool(n2)
print((not (n1 or n2)))