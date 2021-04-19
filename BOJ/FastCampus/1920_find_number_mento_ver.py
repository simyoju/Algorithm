# set 자료형 이용 -> 중복 제거되서 더 빠름
## 백준에 제출해서 비교하니까 빠르기 차이가 엄청남
n = int(input())
array = set(map(int, input().split()))
m = int(input())
x = list(map(int, input().split()))

for i in x:
    if i not in array:
        print('0')
    else:
        print('1')

