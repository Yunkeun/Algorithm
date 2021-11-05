def solution(d, budget):
    answer = 0
    d = sorted(d)
    for x in d:
        if budget < x:
            break
        budget -= x
        answer += 1
    return answer