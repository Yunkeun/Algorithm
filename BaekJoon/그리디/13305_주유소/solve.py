N = int(input())
road_dist = list(map(int, input().split(' ')))
oil_price = list(map(int, input().split(' ')))

total_price = 0
price = oil_price[0]
for i in range(N-1):
    if oil_price[i] < price:
        price = oil_price[i]
    total_price += price * road_dist[i]

print(total_price)