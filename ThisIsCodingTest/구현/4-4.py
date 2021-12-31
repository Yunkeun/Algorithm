# 게임 개발
N, M = map(int, input().split())
A, B, d = map(int, input().split())
direction = [0, 1, 2, 3]
newMap = []
for i in range(N):
    newMap.append(list(map(int, input().split())))
visit = [[A, B]]
rotate =0
count = 0
def getDirection():
    if (d == 0):
        return direction[3]
    return direction[d - 1]
while(True):
    d = getDirection()
    rotate += 1
    if (A != 0 and d == 0 and newMap[A - 1][B] == 0 and ([A - 1, B]) not in visit):
        # 북쪽으로 이동
        A -= 1
        visit.append([A, B])
        count += 1
        rotate = 0
    elif (B != N and d == 1 and newMap[A][B + 1] == 0 and ([A, B + 1]) not in visit):
        # 동쪽으로 이동
        B += 1
        visit.append([A, B])
        count += 1
        rotate = 0
    elif (A != M and d == 2 and newMap[A + 1][B] == 0 and ([A + 1, B]) not in visit):
        # 남쪽으로 이동
        A += 1
        visit.append([A, B])
        count += 1
        rotate = 0
    elif (B != 0 and d == 3 and newMap[A][B - 1] == 0 and ([A, B - 1]) not in visit):
        # 서쪽으로 이동
        B -= 1
        visit.append([A, B])
        count += 1
        rotate = 0
    elif (rotate == 4):
        rotate = 0
        if (A != M and d == 0 and newMap[A + 1][B] == 0):
            # 남쪽으로 이동
            A += 1
            count += 1
        elif (B != 0 and d == 1 and newMap[A][B - 1] == 0):
            # 서쪽으로 이동
            B -= 1
            count += 1
        elif (A != 0 and d == 2 and newMap[A - 1][B] == 0):
            # 북쪽으로 이동
            A -= 1
            count += 1
        elif (B != N and d == 3 and newMap[A][B + 1] == 0):
            # 동쪽으로 이동
            B += 1
            count += 1
        else:
            break
print(count)