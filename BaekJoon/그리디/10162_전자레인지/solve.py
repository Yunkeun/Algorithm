T = int(input())
button_num = [0,0,0,0]
while(1):
    if T == 0:
        break
    elif T < 0:
        button_num[3] += 1
        break
    if T >= 300:
        button_num[0] += 1
        T -= 300
    elif 300 > T >= 60:
        button_num[1] += 1
        T -= 60
    else:
        button_num[2] += 1
        T -= 10
if button_num[3] == 1:
    print(-1)
else:
    for i in range(0,len(button_num)-1):
        print(button_num[i], end=' ')