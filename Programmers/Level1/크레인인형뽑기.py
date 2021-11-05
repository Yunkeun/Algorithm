def solution(board, moves):
    answer = 0
    stack = []
    i = 0
    for num in moves:
        num -= 1
        for line in board:
            if line[num] != 0:
                stack.append(line[num])
                line[num] = 0
                if len(stack)>1 and stack[-1] == stack[-2]:
                    stack.pop()
                    stack.pop()
                    answer += 2
                break
                
    return answer