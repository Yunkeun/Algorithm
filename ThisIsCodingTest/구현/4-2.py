# 시각
h = int(input())
m, n = 59, 59
hour, minute, second = 0, 0, 0
count = 0
while (not(hour == h and minute == m and second == n)):
    if (second == 60):
        minute += 1
        second = 0
    if (minute == 60):
        hour += 1
        minute = 0
    if (str(second).find("3") != -1 or str(minute).find("3") != -1 or str(hour).find("3") != -1):
        count += 1
    second += 1
print(count)