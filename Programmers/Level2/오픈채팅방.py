def solution(record):
    answer = []
    splitted = []
    uid = []
    doing = []
    dict_ = dict()
    new_dict = dict()
    for msg in record:
        splitted = msg.split()
        if msg[0] == 'E':
            doing.append('들어왔습니다.')
            uid.append(splitted[1])
        elif msg[0] == 'L':
            doing.append('나갔습니다.')
            uid.append(splitted[1])
        if len(splitted) == 2:
            dict_ = {splitted[1]: new_dict.get(splitted[1])}
        elif len(splitted) == 3:
            dict_ = {splitted[1]: splitted[2]}
        new_dict.update(dict_)
    n = 0
    for i in uid:
        answer.append(new_dict.get(i) + '님이 ' + doing[n])
        n += 1
    #print(answer)
    return answer