# 점수(0~100 정수)를 입력 받아 평가하여 출력하기
# 90 ~ 100: A
# 70 ~ 89: B
# 40 ~ 69: C
#  0 ~ 39: D
score = int(input())
if 90 <= score <= 100:
    print('A')
elif 70 <= score < 90:
    print('B')
elif 40 <= score < 70:
    print('C')
elif 0 <= score < 40:
    print('D')