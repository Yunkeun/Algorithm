# r, g, b(정수)를 입력 받아 가질 수 있는 색 조합을 오름차순으로 출력하고 마지막에 가짓수 출력하기
r, g, b = map(int, input().split(' '))
n = 0
for i in range(0, r):
    for j in range(0, g):
        for k in range(0, b):
            print(i, j, k)
            n += 1
print(n)
