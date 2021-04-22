import sys
from collections import Counter

N = int(sys.stdin.readline())
cards = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
finded_list = list(map(int, sys.stdin.readline().split()))

counter = Counter(cards)

print(' '.join(str(counter[c]) if c in counter else '0' for c in finded_list))