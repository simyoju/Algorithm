import sys
N = int(sys.stdin.readline())
cards = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
finded_list = list(map(int, sys.stdin.readline().split()))

# result = [0 for _ in range(M)]
result= []

while finded_list:
    std = finded_list.pop(0)
    # print('std: ', std)
    cnt = 0
    for c in cards:
        # print('c: ', c)
        if std == c:
           cnt += 1
    result.append(cnt)

for r in result:
    print(r, end=' ')