A = [0, 3, 3, 7, 5, 3, 11, 1]

def isAdjacent(a, b):
    big = a
    small = b
    if a < b:
        big = b
        small = a
        
    for v in A:
        if small < v and v < big:
            return False
    return True

def getDistance(a, b):
    return abs(a-b)

def solution(A):
    adjacentMinValue = 10000000000
    size = len(A)
    for i in range(size):
        for j in range(i+1, size):
            if isAdjacent(A[i], A[j]):
                distance = getDistance(A[i], A[j])
                if distance == 0:
                    return 0
                if distance < adjacentMinValue:
                    adjacentMinValue = distance
    if adjacentMinValue == 10000000000:
        return -2
    return adjacentMinValue

print(solution(A))