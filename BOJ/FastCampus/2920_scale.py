import sys
# input = sys.stdin.readline

asc = [1, 2, 3, 4, 5, 6, 7, 8]
des = [8, 7, 6, 5, 4, 3, 2, 1]

arr = list(map(int, input().split(' ')))
# arr_int = []
# print(len(arr))
# for a in arr:
#     arr_int.append(int(a))
# print(arr_int)
# print(asc)

# if arr_int == asc:
#     print('ascending')
# elif arr_int == des:
#     print('descending')
# elif sorted(arr_int) == asc:
#     print('mixed')

if arr == asc:
    print('ascending')
elif arr == des:
    print('descending')
elif sorted(arr) == asc:
    print('mixed')