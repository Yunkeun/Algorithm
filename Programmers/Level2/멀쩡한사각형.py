import math

def solution(w,h):
    answer = 1
    gcd = math.gcd(w, h)
    # x, y = w/gcd, h/gcd

    # if x > y:
    #     big = x
    #     small = y
    # else:
    #     big = y
    #     small = x
    #answer = w*h - (math.ceil(big / small) * small * (w/x))
    answer = w*h - (w+h-gcd)

    
    return answer