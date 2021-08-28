# 시작 값(a), 등비(r), 번째 수(n) 을 입력 받아 등비 수열의 n번째 값 출력하기
a, r, n = map(int, input().split(' '))
for i in range(1, n):
    a *= r
print(a)