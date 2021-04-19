# def solution(a):
#
#     cmpStr = a[0]
#     for word in a:
#         ans = 0
#         if word == cmpStr:
#             continue
#         elif word[0] == cmpStr[0]:
#             for c in cmpStr:
#
#             ans += 1
#         else:
#             ans = 0
#             break
#     return ans
#
#
# print(solution(['abcd', 'abce', 'abchg', 'abcfwqw', 'abcdfg'])) #3
# print(solution(['abcd', 'gbce', 'abchg', 'abcfwqw', 'abcdfg'])) #0