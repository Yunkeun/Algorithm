def solution(array, commands):
    answer = []
    for cmd in commands:
        split_arr = array[cmd[0]-1:cmd[1]]
        split_arr.sort()
        answer.append(split_arr[cmd[2]-1])
    return answer