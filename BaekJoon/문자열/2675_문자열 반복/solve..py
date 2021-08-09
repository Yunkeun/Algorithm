T = int(input())                # 테스트 케이스의 개수 T
for i in range(T): 
    num, S = input().split()    # 공백을 기준으로 split
    P = ''                      # 새 문자열 P를 담을 공백
    for i in S:
        P += int(num) * i
    print(P)