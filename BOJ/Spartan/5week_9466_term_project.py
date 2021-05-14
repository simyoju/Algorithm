import sys
sys.setrecursionlimit(111111)
input = sys.stdin.readline

t = int(input())

def dfs(cur):
    global cnt, visited, done
    # 방문처리
    visited[cur] = True
    next = students[cur]
    print(next)
    if not visited[next]:
        dfs(next)
    else:
        if not done[next]: #사이클이 형성되었다.
            i = next
            while i != cur: #팀원 카운트
                cnt += 1
                i = students[i]
            cnt += 1 # 플러스 본인
    done[cur] = True

for _ in range(t):
    n = int(input())
    students = list(map(lambda x : int(x)-1, input().split()))
    visited = [False]*n
    done = [False]*n # 팀 매칭 여부 = 사이클 여부
    cnt = 0
    for i in range(n):
        if not visited[i]: #방문을 안했다면
            dfs(i)
    print(n-cnt)