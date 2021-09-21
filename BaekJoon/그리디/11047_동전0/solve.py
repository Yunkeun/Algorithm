N, K = map(int, input().split(' '))
coins = []
cnt = 0
for i in range(N):
    coin = int(input())
    coins.append(coin)
coins.sort(reverse=True)
for coin in coins:
    cnt += K // coin
    K %= coin
print(cnt)
    