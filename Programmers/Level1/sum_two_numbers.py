def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            answer.append(numbers[i] + numbers[j])
    answer = list(set(answer))
    answer.sort()
    return answer

#print(solution(numbers=[2,1,3,4,1]))
#print(solution(numbers=[5,0,2,7]))
print(solution(numbers=[1,100,100,100,100,100,100,99]))