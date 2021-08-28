# 시작 값(a), 등차(d), 번째 수(n) 을 입력 받아 등차 수열의 n번째 값 출력하기
a, d, n = map(int, input().split()) # 이 문제에서는 split의 괄호를 비워주어야 통과한다.
for i in range(1, n):
    a += d
print(a)