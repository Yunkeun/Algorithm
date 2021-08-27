# 정수를 입력 받아 1부터 해당 수까지 짝수의 합을 구하여 출력하기
num = int(input())
sum = 0
for i in range(1, num+1):
    if i % 2 == 0:
        sum += i
print(sum)