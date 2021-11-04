# 한 문제 시간초과
def solution(N, stages):
    answer = []
    challengers = [0]*(N+1)
    fail = [0]*(N+1)
    fail_rate_dict = {}
    for c_stage in stages:
        for i in range(0, c_stage):
            challengers[i] += 1
            if c_stage-1 == i:
                fail[i] += 1
    for i in range(0, N):
        if challengers[i] == 0:
            fail_rate_dict[i+1] = 0
            continue
        fail_rate_dict[i+1] = fail[i]/challengers[i]
    fail_rate_dict = dict(sorted(fail_rate_dict.items(), key=lambda x: x[1], reverse=True))
    for k in fail_rate_dict:
        answer.append(k)
    return answer

# 다른 사람의 풀이
def solution(N, stages):
    answer = []
    challengers_num = len(stages)
    for c_stage in range(1, N+1):
        fail_count = stages.count(c_stage)
        if fail_count == 0:
            fail = 0
        else:
            fail = fail_count / challengers_num
        answer.append((c_stage, fail))
        challengers_num -= fail_count
    
    answer = sorted(answer, key=lambda t: t[1], reverse=True)
    answer = [i[0] for i in answer]
    return answer

# 참고하여 다시 풀기
def solution(N, stages):
    answer = []
    fail = []
    challengers = []
    challengers_num = len(stages)
    fail_rate_dict = {}
    for c_stage in range(1, N+1):
        fail_count = stages.count(c_stage)
        fail.append(fail_count)
        challengers.append(challengers_num)
        challengers_num -= fail_count
    for i in range(0, N):
        if challengers[i] == 0:
            fail_rate_dict[i+1] = 0
            continue
        fail_rate_dict[i+1] = fail[i]/challengers[i]
    fail_rate_dict = dict(sorted(fail_rate_dict.items(), key=lambda x: x[1], reverse=True))
    for k in fail_rate_dict:
        answer.append(k)
    return answer
