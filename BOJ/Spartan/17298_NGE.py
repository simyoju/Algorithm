# 크기가 N인 수열 A
# 각 원소 Ai에 대해서 오큰수 NGE(i)
# 오큰수 - 오른쪽에 있으면서 Ai보다 큰 수중에 가장 왼쪽에 있는
## 배열 탐색 중에 먼저 마주치는 Ai보다 큰수
# (예외처리) 배열을 다 돌 때까지 그런 수가 없으면 -1 리턴

import sys
N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

stck = []
# 깨달은 부분 : 오큰수를 찾지 못하는 예외 케이슬 둘 것이 아니라,
# 미리 -1 로 다 저장해놓으면 그것이 바로 예외 처리
result = [-1 for _ in range(N)]

stck.append(0)
i = 1

# 배운 부분: 스택에 값이 있고 while stck,
# 인덱스도 사용하려면 and 명령어를 통해 i < N을 써주면 된다.
while stck and i < N:
    # 이해 안가는 부분: 왜 인덱스로 해야하는지 이해가 안감 -_-
    while stck and nums[stck[-1]] < nums[i]:
        print('stck[-1] is ', stck[-1])
        result[stck[-1]] = nums[i]
        stck.pop()

    stck.append(i)
    i += 1

for i in result:
    print(i, end=" ")