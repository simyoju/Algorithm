import sys
N = int(sys.stdin.readline())
arr = list()
sorted_arr = list()

for _ in range(N):
    num = int(sys.stdin.readline())
    arr.append(num)

sorted_arr = sorted(arr)

for sa in sorted_arr:
    print(sa)