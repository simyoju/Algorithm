import sys
input = sys.stdin.readline

test_case = int(input())

def dfs(x, y):
    visited[x][y] = True
    dirs = [(0, 1), (0, -1), (-1, 0), (1, 0)]
    for dx, dy in dirs:
        nx, ny = x + dx, y + dy
        if nx<0 or nx>=n or ny <0 or ny>=m:
            continue
        if plot[nx][ny] and not visited[nx][ny]:
            dfs(nx, ny)

for _ in range(test_case):
    m, n, k = map(int, input().split())
    plot = [[0]*m for _ in range(n)]
    visited = [[False]*m for _ in range(n)]

    for _ in range(k):
        # velog
        # x, y = map(int, input().split())
        y, x = map(int, input().split())
        plot[x][y] = 1
        # print('x, y', x, y)
        print('y, x', y, x)

    print(plot)
    cnt = 0
    for i in range(n):
        for j in range(m):
            if plot[i][j] and not visited[i][j]:
                dfs(i, j)
                cnt += 1

    print(cnt)

