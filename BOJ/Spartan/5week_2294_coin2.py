import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = [0] * n
dp = [10001] * (k+1)
dp[0] = 0
for i in range(n):
    coins[i] = int(input())

coins.sort()
for coin in coins:
    for i in range(coin, k+1):
        dp[i] = min(dp[i-coin]+1, dp[i])

print(dp[-1] if dp[-1] != 10001 else -1)


