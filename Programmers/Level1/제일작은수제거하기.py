def solution(arr):
    if len(arr) == 1:
        return [-1]
    minimum = min(arr)
    index = arr.index(minimum)
    del arr[index]
    return arr