def solution(absolutes, signs):
    sum = 0
    for i, s in enumerate(signs):
        if s == True:
            sum += absolutes[i]
        else:
            sum -= absolutes[i]
    return sum