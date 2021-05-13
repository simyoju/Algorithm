# middle 값 찾고
# N개의 나무에서 뺀값을 더해서 (음수면 포함)
# M과 비교 후 맞으면 출력
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
trees = list(map(int, input().split()))
trees.sort()
# print(trees)

left = 1
right = trees[-1]

while left<=right:
    mid = (left+right)//2
    sum = 0
    # print('mid:',mid)
    for tree in trees:
        if tree >= mid:
            sum += (tree-mid)
    if sum >= M:
        left = mid + 1
    else:
        right = mid - 1

print(right)