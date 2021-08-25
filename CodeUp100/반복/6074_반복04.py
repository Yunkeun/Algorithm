# 문자(a~z)를 입력 받아 a부터 해당 문자까지 출력하기
eng = input()
ord_a = ord('a')
while ord_a <= ord(eng):
    print(chr(ord_a), end=' ')
    ord_a += 1