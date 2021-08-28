# 정수를 입력 받아 1부터 n까지 더한 값이 입력 받은 정수보다 크거나 같은 경우 그때까지의 합 출력하기
num = int(input())
sum = 0
i = 1
while sum < num:
    sum += i
    i += 1
print(sum)