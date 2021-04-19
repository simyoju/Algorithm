N = int(input())

standard = list(map(int, input().split()))

M = int(input())
data = list(map(int, input().split()))

for d in data:
    if d in standard:
        print('1')
    else:
        print('0')

