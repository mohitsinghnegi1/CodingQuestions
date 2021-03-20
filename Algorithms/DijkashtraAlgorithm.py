# dijkashtra algorithm is used to find a distance of every node from sorce node
# dijkashtra algorithm works only in case of positive weights
# to overcome limitation of krushkal algorithm we use belmenford algorithm
# greedy algorithm
# we can use parent array to update node parent


# Qus:https://www.hackerrank.com/challenges/dijkstrashortreach/problem

#!/bin/python

import math
import os
import random
import re
import sys
import sys

from collections import defaultdict
from heapq import heappop, heappush, heapify

# Complete the shortestReach function below.


def shortestReach(n, graph, s):

    dist = [sys.maxsize]*(n+1)

    heap = []
    heapify(heap)

    heappush(heap, (0, s))
    visited = set()
    # print graph
    while(heap):
        pweight, node = heappop(heap)

        if(node in visited):
            continue
        visited.add(node)

        if(n == len(visited)):
            break

        # print "node -> weight ",node,pweight
        for nei, weight in graph[node]:

            if(pweight+weight < dist[nei] and nei not in visited):
                # print "heap",heap

                dist[nei] = pweight+weight
                heappush(heap, (dist[nei], nei))
        out = []
        for i in range(1, n+1):
            if(i != s):
                if(dist[i] == sys.maxsize):
                    out.append(-1)
                else:
                    out.append(dist[i])

    return out


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n, m = map(int, raw_input().split())

        graph = defaultdict(int)

        for _ in range(m):
            u, v, w = map(int, raw_input().rstrip().split())

            if((u, v) in graph):
                graph[(u, v)] = min(graph[(u, v)], w)
                graph[(v, u)] = min(graph[(v, u)], w)
            else:
                graph[(u, v)] = w
                graph[(v, u)] = w

        edges = defaultdict(list)
        for key in graph:
            edges[key[0]].append([key[1], graph[key]])

        # print(edges)

        s = int(input())

        result = shortestReach(n, edges, s)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
