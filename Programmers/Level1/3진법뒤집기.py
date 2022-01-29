def convert(num):
    tmp = '012'
    q, r = divmod(num, 3)
    if q == 0:
        return tmp[r]
    else:
        return convert(q) + tmp[r]
    
def solution(n):
    ternary = convert(n)
    rev = ternary[::-1]
    return int(rev,3)
