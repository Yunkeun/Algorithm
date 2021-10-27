import heapq as hq

def solution(scoville, K):
    answer = 0
    s_heap = []
    for x in scoville:
        hq.heappush(s_heap, x)
    while(s_heap[0] < K):
        #lowest1 = min(s_heap)
        lowest1 = hq.heappop(s_heap)
        #lowest2 = min(s_heap)
        lowest2 = hq.heappop(s_heap)
        hq.heappush(s_heap, lowest1 + lowest2 * 2)
        if (len(s_heap) == 1 and min(s_heap) < K):
            return -1
        answer += 1
    return answer