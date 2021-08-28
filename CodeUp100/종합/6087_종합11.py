# 정수를 입력 받아 입력한 정수까지 출력할 때 3의 배수를 제외하고 출력하기
i = int(input())
for i in range(1, i+1):
    if i % 3 == 0:
        pass
    else:
        print(i, end=' ')