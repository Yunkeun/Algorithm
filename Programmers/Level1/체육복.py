def solution(n, lost, reserve):
    arr = [1] * n
    for i in lost:
        arr[i-1] = 0
    for i in reserve:
        arr[i-1] = 2
    for i in reserve:
        for j in lost:
            if (i == j):
                arr[i-1] = 1
    num = 1
    for i in range(2, n):
        if (arr[i] == 2):
            if (arr[i-1] == 0):
                arr[i] = 1
                arr[i-1] = 1
    for i in range(0, n-1):
        if ((arr[i] == 2) & (arr[i+1] == 0)):
            arr[i] = 1
            arr[i+1] = 1
    if ((arr[1] == 2) & (arr[0] == 0)):
        arr[1] = 1
        arr[0] = 1
    #print(arr)
    answer = 0
    for i in arr:
        if (i >= 1):
            answer += 1
            
    return answer