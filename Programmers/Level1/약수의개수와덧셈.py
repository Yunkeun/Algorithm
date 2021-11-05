import math

def get_divisor_num(num):
    cnt = 0
    for i in range(1, int(math.sqrt(num))+1):
        if num % i == 0:
            cnt += 1
    if num % math.sqrt(num) == 0:
        cnt -= 1
        cnt *= 2
        cnt += 1
    else:
        cnt *=2
    return cnt

def solution(left, right):
    answer = 0
    for num in range(left, right+1):
        if get_divisor_num(num) % 2 == 0:
            answer += num
        else:
            answer -= num
    return answer

# 천재들의 풀이
def solution(left, right):
    answer = 0
    for num in range(left, right+1):
        if int(num ** 0.5) == num ** 0.5:
            answer -= num
        else:
            answer += num
    return answer