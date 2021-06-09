def solution(arr):
    answer = []
    # 순서를 유지하는 것이 관건. set은 자동 정렬이 되어서 안될 듯
    for i in range(len(arr)):
        a = arr[i]
        if i+1 < len(arr):
            next_a = arr[i+1]
        else:
            answer.append(a)

        if a != next_a:
            answer.append(a)

        print(a)
    return answer

print(solution(arr=[4,4,4,3,3]))