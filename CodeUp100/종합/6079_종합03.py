# 정수를 입력 받아 해당 수가 1부터 n까지 더한 값보다 같거나 커졌을 때의 n값 구하여 출력하기
max = int(input())
sum = 0
n = 0
while sum < max:
    n += 1
    sum += n
print(n)