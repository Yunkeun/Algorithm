def solution(s):
    stack = []
    for i in range(len(s)):
        # 스택이 비어있다면 append
        if not stack:
            stack.append(s[i])
        else:
            # 스택의 마지막과 현재의 문자와 같다면 pop
            if stack[-1] == s[i]:
                stack.pop()
            # 다르다면 append
            else:
                stack.append(s[i])
    # 스택이 비어있다면 (전부 pop) 1리턴 (성공)
    if not stack:
        return 1
    else:
        return 0