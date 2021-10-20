def solution(lottos, win_nums):
    answer = []
    high_rank = 6
    low_rank = 6
    match_num = 0
    zero_cnt = 0
    for num in lottos:
        if num in win_nums:
            match_num += 1
        if num == 0:
            zero_cnt += 1
    if match_num < 2:
        low_rank = 6
    else:
        low_rank = low_rank - match_num + 1
    high_rank = low_rank - zero_cnt
    if zero_cnt == 6:
        high_rank = 1
    answer = [high_rank, low_rank]
    return answer

def solution2(lottos, win_nums):
    rank = [6,6,5,4,3,2,1]

    cnt_zero = lottos.count(0)
    ans = 0
    for num in win_nums:
        if num in lottos:
            ans += 1
    return rank[cnt_zero + ans], rank[ans]