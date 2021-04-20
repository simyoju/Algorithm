n = int(input())

num = []
sorted_num = []
print(n)
for _ in range(n):
    data = int(input())
    num.append(data)

sorted_num = sorted(num)

for n in sorted_num:
    print(n)
    # print()
