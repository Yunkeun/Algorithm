# 정수 두 개를 입력 받아 두 정수 중 하나라도 True라면 True, 아니라면 False 출력하기
n1, n2 = map(int, input().split(' '))
print(bool(n1 or n2))