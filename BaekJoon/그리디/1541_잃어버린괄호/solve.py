equation = input().split('-')
sum = 0
for num in equation[0].split('+'):
    sum += int(num)
for insideEquation in equation[1:]:
    for num in insideEquation.split('+'):
        sum -= int(num)

print(sum)