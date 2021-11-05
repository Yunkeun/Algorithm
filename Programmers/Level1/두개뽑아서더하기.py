def solution(numbers):
    answer = []
    len_num = len(numbers)
    for i in range(len_num):
        for j in range(i+1, len_num):
            answer.append(numbers[i]+numbers[j])
    answer = list(sorted(set(answer)))
    return answer