from collections import deque
import sys
input = sys.stdin.readline

test_case = int(input())

def bfs(x, y):
    directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]

    que = deque()
    que.append((x, y))

    plot[x][y] = 0

    while que:
        n = que.popleft()

        for i in range(4):
            nx = n[0] + directions[i][0]
            ny = n[1] + directions[i][1]

            if (0<=nx<N) and (0<=ny<M):
                if plot[nx][ny] == 1:
                    plot[nx][ny] = 0
                    que.append((nx, ny))

for _ in range(test_case):
    M, N, K = map(int, input().split())
    # print(M, N, K)
    plot = [[0]*51 for _ in range(51)]
    cnt = 0

    for _ in range(K):
        x, y = map(int, input().split())
        # print(x, y)
        plot[x][y] = 1

    # print(plot)
    for i in range(N):
        for j in range(M):
            if plot[i][j] == 1:
                cnt += 1
                bfs(i, j)

    print(cnt)