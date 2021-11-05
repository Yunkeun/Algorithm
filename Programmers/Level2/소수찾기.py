from itertools import permutations
import math

def check_prime(number):
    if number == 0 or number == 1:
        return False
    for n in range(2, int(math.sqrt(number))+1):
        if number % n == 0:
            return False
    return True

def solution(numbers):
    answer = 0
    arr_num = []
    for i in range(len(numbers)):
        permu_num = permutations(numbers, i+1)
        for x in permu_num:
            arr_num.append(int("".join(x)))
    arr_num = list(set(arr_num))
    for num in arr_num:
        if check_prime(int(num)):
            answer +=1
    return answer