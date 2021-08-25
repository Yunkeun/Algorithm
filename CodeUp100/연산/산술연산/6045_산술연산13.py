# 정수 세 개를 입력 받아 공백을 두고 합과 평균(소수 둘째 자리까지) 출력하기
n1, n2, n3 = map(int, input().split(' '))
sum = n1 + n2 + n3
mean = format(float(sum / 3), '0.2f')
print(sum, mean)