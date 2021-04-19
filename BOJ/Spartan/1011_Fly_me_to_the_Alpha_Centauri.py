t = int(input())

for _ in range(t):
    x, y = map(int, input().split())
    cnt = 0

    arr = [x, x+1, x+2]

    for a in arr:
        cnt += 1
        if a == y:
            print(cnt)
    cnt = 0

    x += 1
    arr = [x, x+1, x+2]

