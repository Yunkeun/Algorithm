# 정수를 입력 받아 음/양/짝/홀을 구분하여 출력하기
# 음의 짝수: A
# 음의 홀수: B
# 양의 짝수: C
# 양의 홀수: D
num = int(input())
if num < 0:
    if num % 2 == 0:
        print('A')
    else:
        print('B')
else:
    if num % 2 == 0:
        print('C')
    else:
        print('D')