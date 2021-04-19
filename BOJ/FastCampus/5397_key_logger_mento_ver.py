# 스택 자료구조 두개 이용하면 간단히 풀린다 !

test_case = int(input())

for _ in range(test_case):
    left_stack = []
    right_stack = []

    data = input()
    for i in data:
        if i == '-':
            if left_stack:
                left_stack.pop()
        elif i == '<':
            if left_stack:
                right_stack.append(left_stack.pop())
        elif i == '>':
            if right_stack:
                left_stack.append(right_stack.pop())
        else:
            left_stack.append(i)
    left_stack.extend(reversed(right_stack))
    print(''.join(left_stack))