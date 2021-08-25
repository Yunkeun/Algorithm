# 정수 두 개(n1 n2)를 입력 받아 n1과 2의 n2 거듭 제곱의 곱을 곱하여 출력하기
n1, n2 = map(int, input().split(' '))
n2 = 1 << n2
res = n1 * n2
print(res)