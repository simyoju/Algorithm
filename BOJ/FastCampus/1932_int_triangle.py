import sys
input = sys.stdin.readline

N = int(input())
arr = [[0 for _ in range(N+1)] for _ in range(N+1)]
DP = [[0 for _ in range(N+1)] for _ in range(N+1)]

# 입력
for i in range(1, N+1):
    tmp = list(map(int, input().split()))
    for j in range(1, i+1):
        arr[i][j] = tmp[j-1]

# 반복문을 위에서부터 아래로 쭉 돌자
for i in range(1, N+1):
    for j in range(1, i+1):
        DP[i][j] = max(DP[i-1][j-1], DP[i-1][j]) + arr[i][j]

print(max(DP[-1]))
