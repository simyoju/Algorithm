import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    cmd_p = input()
    n = int(input())
    arr = input()[1:-2].split(',')
    cmd_p = cmd_p.replace('RR','') #R이 두번이면 원상 복구 되므로 명령어에서 제거

    cntR = 0
    delF, delB = 0, 0 # R의 개수에 따라 앞에서 제거할지 뒤에서 제거할지 세는 변수

    for cmd in cmd_p:
        if cmd == 'R':
            cntR += 1
        elif cmd == 'D':
            if cntR%2 == 0:
                delF += 1
            else:
                delB += 1

    if delF+delB <= n:
        arr = arr[delF:n-delB]

        if cntR%2 == 1:
            print('[' + ','.join(arr[::-1]) + ']')
        else:
            print('[' + ','.join(arr) + ']')
    else:
        print('error')



