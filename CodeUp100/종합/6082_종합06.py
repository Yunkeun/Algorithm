# 정수(1~29)를 입력 받아 369 게임 출력하기, 이때 박수 대신 X 출력하기
max = int(input())
for i in range(1, max+1):
    s = str(i)
    if i < 10 and i % 3 == 0:
        print('X', end=' ')
    elif i >= 10 and (s[1] == '3' or s[1] == '6' or s[1] == '9'):
        print('X', end=' ')
    else:
        print(i, end=' ')

# if i % 10 == 3 or i % 10 == 6 or i % 10 == 9: