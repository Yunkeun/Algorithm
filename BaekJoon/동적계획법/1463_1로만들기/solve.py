# n=1 -> 0
# n=2 -> 1
# n=3 -> 1
# n=4 -> 1+(n=2결과)
# n=5 -> 1+(n=4결과)
# n=6 -> 1+(n=2결과)

n = int(input())
dp = [0] * (n+1)
dp[2] = 1
dp[3] = 1
for i in range(4, n+1):
    dp[i] = dp[i-1] + 1
    if i % 2 == 0:
        dp[i] = min(dp[i], 1+dp[i//2])
    if i % 3 == 0:
        dp[i] = min(dp[i], 1+dp[i//3])
    print(dp)
print(dp[n])