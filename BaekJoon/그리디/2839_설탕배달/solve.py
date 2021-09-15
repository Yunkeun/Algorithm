# if 5로 나누어 떨어진다: cnt += 몫 
# else:
    # 3kg 봉지 하나 추가 (sugar -= 3, cnt++)

sugar = int(input())
cnt = 0
while(sugar):
    if sugar % 5 == 0:
        cnt += sugar // 5
        break
    else:
        sugar -= 3
        cnt += 1
    if sugar < 0:
        cnt = -1
        break
print(cnt)