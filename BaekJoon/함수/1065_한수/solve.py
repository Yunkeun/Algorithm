def hansoo(num):
    h = 0

    for i in range(1, num + 1):
        if (i <= 99):
            h += 1
        else:
            list_num = list(map(int, str(i)))
            if (list_num[0] - list_num[1] == list_num[1] - list_num[2]):
                h += 1
    return h