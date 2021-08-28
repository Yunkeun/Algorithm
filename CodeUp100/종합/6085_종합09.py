# w, h, b 를 입력 받아 MB로 환산하여 출력하기
w, h, b = map(int, input().split(' '))
storage = w * h * b / 8 / 1024 / 1024
storage = format(storage, '0.2f')
print(storage, 'MB')