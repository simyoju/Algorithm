# 스택에서 원소를 연달아 빼낼 때, 내림차순을 유지할 수 있는지 확인하는 것이 중
n = int(input())

cnt = 1
stck = []
ans = []

for i in range(1, n+1): #데이터 개수만큼 반복
    data = int(input())

    while cnt <= data:
        stck.append(cnt)
        cnt += 1
        ans.append('+')

    if stck[-1] == data:
            stck.pop()
            ans.append('-')
    else:
            print('NO')
            exit(0)

print('\n'.join(ans))


