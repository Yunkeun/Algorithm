# 문자를 입력 받아 다음 문자 출력하기
c = input()
to_ord = ord(c)
next_c = chr(to_ord + 1)
print(next_c)