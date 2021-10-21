def solution(new_id):
    answer = ""
    dot_num = 0
    # 1
    new_id = new_id.lower()
    # 2
    available_char = "-_.abcdefghijklmnopqrstuvwxyz0123456789"
    new_id = ''.join(x for x in new_id if x in available_char)
    # 3
    for c in new_id:
        if c == '.':
            dot_num += 1
        else:
            dot_num = 0
        if dot_num > 1:
            continue
        else:
            answer += c
    # 4
    if answer[0] == '.':
        answer = answer[1:]
    if answer[-1:] == '.':
        answer = answer[:-1]
    # 5
    if answer == "":
        answer = "a"
    # 6
    if len(answer) > 15:
        answer = answer[:15]
    if answer[-1:] == '.':
        answer = answer[:-1]
    # 7
    while (len(answer) < 3):
        answer += answer[-1:]
        
    return answer

def solution2(new_id):
    answer = ''
    # 1
    new_id = new_id.lower()
    # 2
    for c in new_id:
        if c.isalpha() or c.isdigit() or c in ['-', '_', '.']:
            answer += c
    # 3
    while '..' in answer:
        answer = answer.replace('..', '.')
    # 4
    if answer[0] == '.':
        answer = answer[1:] if len(answer) > 1 else '.'
    if answer[-1] == '.':
        answer = answer[:-1]
    # 5
    if answer == '':
        answer = 'a'
    # 6
    if len(answer) > 15:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]
    # 7
    while len(answer) < 3:
        answer += answer[-1]
    return answer