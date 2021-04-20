import sys
import math
from collections import defaultdict, deque
from heapq import heapify, heapify, heappop, heappush, heapreplace, heappushpop


def getNo(a):
    count = 0
    for i in a:
        count += i
        if(i % 2):
            return count
    return count


t = int(input())

for i in range(t):
    n, q = map(int, raw_input().split())
    a = map(int, raw_input().split())

    print getNo(sorted(a, reverse=True))

    for i in range(q):
        x, v = map(int, raw_input().split())
        a[x-1] = v
        print getNo(sorted(a, reverse=True))
