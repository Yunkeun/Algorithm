# 16진수를 입력 받아 입력한 정수의 16진수 구구단 출력하기
h = input()
num = int(h, 16)
for i in range(1, 16):
    res = i * num
    print('%X*%X=%X'%(num,i,res))