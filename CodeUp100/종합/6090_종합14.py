# 시작 값(a), 곱할 값(r), 더할 값(d), 번째 수(n) 을 입력 받아 등차등비 수열의 n번째 값 출력하기
a, r, d, n = map(int, input().split())
for i in range(1, n):
    a *= r
    a += d
print(a)