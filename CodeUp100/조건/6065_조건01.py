# 세 정수를 입력 받아 짝수만 출력하기
n1, n2, n3 = map(int, input().split(' '))
if n1 % 2 == 0:
    print(n1)
if n2 % 2 == 0:
    print(n2)
if n3 % 2 == 0:
    print(n3)