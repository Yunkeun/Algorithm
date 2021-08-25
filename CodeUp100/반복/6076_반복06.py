# 정수를 입력 받아 0부터 해당 정수까지 출력하기 (range() 사용)
num = int(input())
start = 0
for i in range(start, num + 1, 1):
    print(i)

# range(시작, 끝, 증가폭)