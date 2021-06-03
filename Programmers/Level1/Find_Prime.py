def isPrime(n):
    for i in range(2, n+1):
        if i*i <= n:
            if n%i == 0:
                return False
    return True


def solution(n):
    answer = 0
    for i in range(2, n+1):
        if isPrime(i) == True:
            answer += 1
            #print(i)
    return answer

print(solution(n=10))