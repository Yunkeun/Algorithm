# h, b, c, s 를 입력 받아 MB로 환산하여 출력하기
h, b, c, s = map(int, input().split(' '))
space = h * b * c * s / 8 / 1024 / 1024
space = format(space, ('0.1f'))
print(space, 'MB')