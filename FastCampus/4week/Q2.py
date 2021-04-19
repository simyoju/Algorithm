def countUniques(a):
    ans_list = []
    for num in a:
        if num not in ans_list:
            ans_list.append(num)
    # print(ans_list)
    return len(ans_list)

# Test code
print(countUniques([-1, 1, 1, 1, 1, 4, 4, 4, 4, 10, 14, 14]))  # 5
print(countUniques([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]))  # 2