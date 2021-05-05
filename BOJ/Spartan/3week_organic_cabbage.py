from collections import deque
import sys
input = sys.stdin.readline

test_case = int(input())

def bfs(x, y):
    directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]

    que = deque()
    que.append((x, y))
    # print(que)

    # plot[x][y] = 0
    visited[x][y] = True

    while que:
        n = que.popleft()
        # print('n: ', n)

        for i in range(4):
            nx = n[0] + directions[i][0]
            ny = n[1] + directions[i][1]

            if (0<=nx<M) and (0<=ny<N):
                if plot[nx][ny] == 1 and visited[nx][ny] == False:
                    visited[nx][ny] = True
                    que.append((nx, ny))

for _ in range(test_case):
    M, N, K = map(int, input().split())
    # print(M, N, K)
    plot = [[[0]*M] for _ in range(N)]
    visited = [[False]*M for _ in range(N)]
    cnt = 0

    for _ in range(K):
        x, y = map(int, input().split())
        # print(x, y)
        plot[y][x] = 1

    # print(plot)
    for i in range(N):
        for j in range(M):
            if plot[i][j] == 1 and visited:
                # print('i, j: ', i, j)
                cnt += 1
                bfs(i, j, visited)
    # print(plot)
    print(cnt)