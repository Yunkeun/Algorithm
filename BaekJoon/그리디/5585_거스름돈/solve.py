price = int(input())
coin_types = [500, 100, 50, 10, 5, 1]
change = 1000 - price
cnt = 0
for coin in coin_types:
    cnt += change // coin
    change %= coin
print(cnt)