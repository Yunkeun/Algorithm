def solution(arr):
    answer = [arr[0]]
    for i in range(1, len(arr)):
        length = len(answer)
        if arr[i] == arr[i-1]:
            continue
        if arr[i] != arr[i-1]:
            if answer[length-1] != arr[i]:
                answer.append(arr[i])
    return answer