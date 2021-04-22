# 크기가 N인 수열 A
# 각 원소 Ai에 대해서 오큰수 NGE(i)
# 오큰수 - 오른쪽에 있으면서 Ai보다 큰 수중에 가장 왼쪽에 있는
## 배열 탐색 중에 먼저 마주치는 Ai보다 큰수
# (예외처리) 배열을 다 돌 때까지 그런 수가 없으면 -1 리턴


import sys
arr_NGE = list()

def NGE(arr):
    for i in range(len(arr)):
        std_i = arr[i]
        for j in range(i, len(arr)):
            if std_i < arr[j]:
                arr_NGE.append(arr[j])
                break
            elif j == (len(arr)-1):
                arr_NGE.append(-1)

N = int(sys.stdin.readline())
arr_A = list(map(int ,sys.stdin.readline().split()))
# for _ in range(N):
NGE(arr_A)
for a in arr_NGE:
    print(a, end=" ")