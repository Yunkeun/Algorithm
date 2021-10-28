def solution(numbers, hand):
    answer = ''
    left = 10
    right = 12
    distLR = [0,0]
    dist = [0,0]
    n = 0
    for i, num in enumerate(numbers):
        if num % 3 == 1:
            left = num
            answer += 'L'
        elif num % 3 == 0 and num != 0:
            right = num
            answer += 'R'
        else:
            if num == 0:
                n = 11
            else:
                n = num
            for j, c in enumerate(answer):
                if c == 'L':
                    if numbers[j] == 0:
                        left = 11
                    else:
                        left = numbers[j]
                else:
                    if numbers[j] == 0:
                        right = 11
                    else:
                        right = numbers[j]
            distLR[0] = abs(n - left)
            distLR[1] = abs(n - right)
            for i, d in enumerate(distLR):
                if d == 1 or d == 3:
                    dist[i] = 1
                elif d == 2 or d == 4:
                    dist[i] = 2
                elif d == 5 or d == 7:
                    dist[i] = 5
                elif d == 6:
                    dist[i] = 4
                elif d == 9:
                    dist[i] = 9
                elif d == 8 or d == 10:
                    dist[i] = 17
                else:
                    dist[i] = 0
            if dist[0] < dist[1]:
                answer += 'L'
            elif dist[0] > dist[1]:
                answer += 'R'
            else:
                if hand == "right":
                    answer += 'R'
                else:
                    answer += 'L'
    return answer