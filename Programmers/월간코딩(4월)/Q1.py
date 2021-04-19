import sys

abs = [4, 7, 12]
signs = [True, False, True]
def solution(absolutes, signs):
    answer = 0
    idx = 0
    for s in signs:
        if s == 0:
            answer -= abs[idx]
        else:
            answer += abs[idx]
        idx += 1
        # print(answer)
    return answer

solution(abs, signs)