N, K = map(int, input().split(' '))
coin_types = []
# changes minimum
for i in range(N):
    coin = int(input())
    coin_types.append(coin)

cnt = 0
# From the biggest type to smallest type, 
coin_types.sort(reverse=True)
for coin in coin_types:
    cnt += K // coin
    K %= coin
print(cnt)