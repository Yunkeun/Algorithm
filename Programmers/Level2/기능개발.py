import math

def solution(progresses, speeds):
    answer = []
    remain_days = []
    cnt = 1
    for i in range(len(progresses)):
        day = math.ceil((100-progresses[i])/speeds[i])
        remain_days.append(math.ceil((100-progresses[i])/speeds[i]))
    front = 0
    for i in range(len(remain_days)):
        if remain_days[i] > remain_days[front]:
            answer.append(i-front)
            front = i
    answer.append(len(remain_days)-front)
    return answer