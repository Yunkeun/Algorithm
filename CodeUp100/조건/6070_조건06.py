# 정수를 입력 받아 알맞은 계절 출력하기
# 12, 1, 2: winter
# 3, 4, 5: spring
# 6, 7, 8: summer
# 9, 10, 11: fall
m = int(input())
if m // 3 == 1:
    print('spring')
elif m // 3 == 2:
    print('summer')
elif m // 3 == 3:
    print('fall')
else:
    print('winter')