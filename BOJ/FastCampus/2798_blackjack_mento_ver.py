# 조합을 기억하고 그 식도 기억해서 주어지는 케이스 수를 보고 시간초과가 될지 생각
# 3개를 뽑는 조합 경우의 수 식 ((n-2)(n-1)n)/3!
# 파이썬은 1초에 2000만 정도 수식 해결 -> 이번 문제의 케이스는 완전탐색으로 풀어도 시간초과가 안나니 그렇게 푼다

n, m = list(map(int, input().split(' ')))
data = list(map(int, input().split(' ')))

ans = 0
len = len(data)
for i in range(0, len):
    for j in range(i+1, len):
        for k in range(j+1, len):
            sum = data[i] + data[j] + data[k]
            if sum <= m:
                ans = max(ans, sum)

print(ans)
