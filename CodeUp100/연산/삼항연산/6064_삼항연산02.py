# 삼항연산을 이용하여 세 정수 중 가장 작은 값 출력하기
n1, n2, n3 = map(int, input().split(' '))
# smallest = n1 if (n1 < n2) & (n1 < n3) else n2 if (n2 < n1) & (n2 < n3) else n3
smaller = n1 if (n1 < n2) else n2
smallest = n3 if (n3 < smaller) else smaller
print(smallest)