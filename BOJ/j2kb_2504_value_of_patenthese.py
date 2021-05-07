import sys
input = sys.stdin.readline
str = input()
stack = []
cur = 1
res = 0

for i in range(len(str)):
    if str[i] == ']' or str[i] == ')':
        if not stack:
            print(0)

    if str[i] == '(':
        stack.append('(')
        cur = cur * 2
        if i + 1 < len(str) and str[i + 1] == ')':
            res += cur

    elif str[i] == '[':
        stack.append('[')
        cur = cur * 3
        if i + 1 < len(str) and str[i + 1] == ']':
            res += cur

    if stack:
        if str[i] == ')':
            cur = cur // 2
            if stack[-1] == '(':
                stack.pop()
        elif str[i] == ']':
            cur = cur // 3
            if stack[-1] == '[':
                stack.pop()

if stack:
    print(0)

print(res)