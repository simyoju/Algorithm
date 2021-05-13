import sys
import collections
input = sys.stdin.readline

N = int(input())
cardList = []
for _ in range(N):
    cardList.append(int(input()))

counter = collections.Counter(cardList)
counter = dict(sorted(counter.items()))
# print(counter)
print(max(counter, key=counter.get))