def isPrimeNumber(number):
    if number == 1:
        return False
    elif number == 2:
        return True
    else:
        if number % 2 == 0:
            return False
    for n in range(3, number, 2):
        if number % n == 0:
            return False
    return True

def solution(nums):
    count = 0
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            for k in range(j+1, len(nums)):
                if isPrimeNumber(nums[i]+nums[j]+nums[k]):
                    count += 1
    

    return count