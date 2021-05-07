import sys
input = sys.stdin.readline

n = int(input())
arr = list(input().split())
dp = [0 for _ in range(n)]
ans = [0 for _ in range(n)]

for i in range(n):
    arr[i] = int(arr[i])

for i in range(1, n):
    dp[i-1] = arr[i-1]
    for j in range(i, n):
        cur = dp[j-1] + arr[j]
        print(cur, j)
        if cur < arr[j]:
            ans[i-1] = dp[j-1]
            break
        dp[j] = cur
    dp = [0 for _ in range(n)]

print(ans)
print(max(ans))