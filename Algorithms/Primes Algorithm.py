"""
    No need to detect cycle using union find in primes and dijkastra
    it is similar to bfs but using heap and visited
    check if node already in visited then dont triverse , set elemtn in visited list only after processing it (after poping from the heap)
"""


# Qus:https://www.hackerearth.com/practice/algorithms/graphs/minimum-spanning-tree/tutorial/

# Write your code here
import sys
from collections import defaultdict
from heapq import heappop, heappush
n, m = list(map(int, raw_input().split()))
graph = defaultdict(list)

for i in range(m):
    u, v, w = map(int, raw_input().split())
    graph[u-1].append([v-1, w])
    graph[v-1].append([u-1, w])

# graph is ready


def primes(graph):
    visited = set()
    heap = []
    heappush(heap, (0, 0))
    cost = 0
    while(heap):
        curwgt, src = heappop(heap)

        if(src in visited):
            continue

        visited.add(src)
        cost += curwgt

        for dest, w in graph[src]:

            if(dest not in visited):
                heappush(heap, (w, dest))
    return cost


print primes(graph)
