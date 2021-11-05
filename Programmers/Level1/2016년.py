def solution(a, b):
    answer = ''
    week = ['THU','FRI','SAT','SUN','MON','TUE','WED']
    last_day = [31,29,31,30,31,30,31,31,30,31,30,31]
    total_day = 0
    for i in range(0,a-1):
        total_day += last_day[i]
    total_day += b
    answer = week[total_day%7]
    return answer