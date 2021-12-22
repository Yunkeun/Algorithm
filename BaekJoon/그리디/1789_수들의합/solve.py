s = int(input())
n = 0
res = 0
for i in range(1, s+1):
    res += i
    n += 1
    if (res > s):
        break
print(n - 1)