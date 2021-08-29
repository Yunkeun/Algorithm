# 정수를 입력 받아 입력 받은 수 만큼 숫자를 입력 받아 그 수들을 거꾸로 출력하기
n = int(input())
lst = list(map(int, input().split()))
for i in reversed(lst):
    print(i, end=' ')