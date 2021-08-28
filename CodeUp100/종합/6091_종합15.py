# d1, d2, d3 세 방문 주기를 입력 받아 다시 모두 방문하는 날짜 구하여 출력하기
d1, d2, d3 = map(int, input().split(' '))
n = 1
while True:
    if (n % d1) == 0 and (n % d2 == 0) and (n % d3 == 0):
        break
    n += 1
print(n)