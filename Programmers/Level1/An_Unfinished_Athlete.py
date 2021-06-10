def solution(participant, completion):
    answer = ''
    participant.sort()
    completion.sort(reverse=1)
    print(participant, completion)

    complete = completion.pop()

    for p in participant:
        if complete == p:
            if len(completion) != 0:
                complete = completion.pop()
        else:
            answer += p

    return answer

print(solution(participant=["mislav", "stanko", "mislav", "ana"], completion=["stanko", "ana", "mislav"]))