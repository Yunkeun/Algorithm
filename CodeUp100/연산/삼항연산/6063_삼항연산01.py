# 삼항연산을 이용하여 두 정수 중 큰 값 출력하기
n1, n2 = map(int, input().split(' '))
bigger = n1 if n1 > n2 else n2
print(bigger)