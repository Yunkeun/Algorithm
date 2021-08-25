# 정수 두 개를 입력 받아 각 줄에 합, 차, 곱, 몫, 나머지, 나눈값(실수로 소수 둘째 자리까지) 출력하기
n1, n2 = map(int, input().split(' '))
print(n1 + n2)
print(n1 - n2)
print(n1 * n2)
print(n1 // n2)
print(n1 % n2)
print(format(float(n1 / n2), '0.2f'))