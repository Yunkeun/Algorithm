# 정수 0이 입력될 때까지 입력되는 정수 계속 출력하기
num = 1
while True:
    num = int(input())
    if num != 0:
        print(num)
    else:
        break