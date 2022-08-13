def check(turnOn, turnOnNumber, index):
    for i in range(turnOnNumber, index):
        if turnOn[i] == False:
            return False
    return True

def solution(A):
    # write your code in Python 3.6
    count = 0
    turnOn = [False] * len(A)
    turnOnNumber = 0

    for v in A:
        turnOn[v-1] = True
        if check(turnOn, turnOnNumber, v-1):
            turnOnNumber = v-1
            count += 1
    return count