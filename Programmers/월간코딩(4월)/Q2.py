parenth = "[](){}"

def solution(s):
    answer = -1
    trans_parenth = parenth
    for i in range(0, s):
        print('변형 전: ', trans_parenth)
        front_p = trans_parenth[0]
        print(front_p)
        trans_parenth = parenth[1:-1] + front_p
        print(trans_parenth)
    # for p in parenth:
    #     print(front_p)
    return answer

solution(3)