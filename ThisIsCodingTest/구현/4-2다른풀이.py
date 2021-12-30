# 시각
hour = int(input())
count = 0
maximum_minute = 60
maximum_second = 60
for h in range(hour + 1):
    for m in range(maximum_minute):
        for s in range(maximum_second):
            if ('3' in str(h) + str(m) + str(s)):
                count += 1
print(count)