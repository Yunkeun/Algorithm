N = input()
N = sorted(N, reverse=True)
if '0' not in N:
    print(-1)
else:
    sum = 0
    for i in N:
        sum += int(i)
    if sum % 3 == 0:
        print(''.join(N))
    else:
        print(-1)