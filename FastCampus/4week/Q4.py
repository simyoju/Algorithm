def solution(n):
    while n > 9:
        n = sum([int(i)**2 for i in str(n)])
        # print(n)
        if n == 1:
            return True
        else:
            solution(n)
    return False

print(solution(19))
print(solution(61))

