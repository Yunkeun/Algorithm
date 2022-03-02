N = int(input())

checkList = [0] * 10001
for i in range(N):
    inputNum = int(input())

    checkList[inputNum] = checkList[inputNum] + 1
for i in range(10001):
    if checkList[i] != 0:
        for j in range(checkList[i]):
            print(i)