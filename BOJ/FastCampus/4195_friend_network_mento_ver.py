# Union-Find 알고리즘 이용 (합집합)
## 원소들의 연결 여부를 확인하는 알고리즘
## 부모테이블을 이용해서 본인이 어디 속해있는지 파악하는

def find(x):
    if x == parent[x]:
        return x
    else:
        p = find(parent[x])
        parent[x] = p
        return parent[x]

def union(x, y):
    x = find(x)
    y = find(y)

    if x != y:
        parent[y] = x
        number[x] += number[y]

test_case = int(input())

for _ in range(test_case):
    # input이 str이기 때문에 리스트로 만들 수 없고
    # dict을 통해 만들어 주는게 효과적
    parent = dict()
    number = dict()

    f = int(input())

    for _ in range(f):
        x, y = input().split(' ')

        if x not in parent:
            parent[x] = x
            number[x] = 1
        if y not in parent:
            parent[y] = y
            number[y] = 1

        union(x, y)
        print(number[find(x)])