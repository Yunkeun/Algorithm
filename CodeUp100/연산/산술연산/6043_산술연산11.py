# 실수 두 개 입력 받아 나눈 결과를 소숫점 셋째 자리까지 반올림하여 출력하기
f1, f2 = map(float, input().split(' '))
res = format(f1 / f2, ('0.3f'))
print(res)