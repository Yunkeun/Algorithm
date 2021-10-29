def solution(numbers):
    answer = -1
    number_list = [1,2,3,4,5,6,7,8,9]
    sum = 0
    for num in number_list:
        if num not in numbers:
            sum += num
    return sum