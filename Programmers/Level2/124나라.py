def solution(n):
    answer = ''
    ans = []
    while(True):
        quotient = (n-1) // 3
        remainder = (n-1) % 3
        if (remainder == 0):
            ans.append("1")
        elif (remainder == 1):
            ans.append("2")
        else:
            ans.append("4")
        if (quotient <= 0):
            break
        n = quotient
        
    ans = list(reversed(ans))
    answer = "".join(ans)
    return answer