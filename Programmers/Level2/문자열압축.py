def solution(s):
    answer = 10000
    split_num = []
    cnt = 1
    for n in range(1, len(s)//2+1):
        split_token = []
        string = ""
        token = s[:n]

        for i in range(n, len(s)+n, n):
            if (token == s[i:i+n]):
                cnt += 1
            else:
                if cnt > 1:
                    string += str(cnt)+token
                else:
                    string += token
                token = s[i:i+n]
                cnt = 1
        answer = min(answer, len(string))
        
    if len(s) == 1:
        answer = 1
    return answer