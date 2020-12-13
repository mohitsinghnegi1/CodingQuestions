# QUs:https://leetcode.com/problems/path-with-maximum-probability/
from heapq import heappop, heappush
from collections import defaultdict


class Solution(object):
    def maxProbability(self, n, edges, succProb, start, end):
        """
        :type n: int
        :type edges: List[List[int]]
        :type succProb: List[float]
        :type start: int
        :type end: int
        :rtype: float
        """
        """
            probability will be max ,so we will heapify using probability
            This is similar to dijkastra but in this instead of min dist we need to
            find the max dist where dist = probability and probability should be max
        
        """

        # construct a graph
        d = defaultdict(list)
        for i in range(len(edges)):
            d[edges[i][0]].append((edges[i][1], succProb[i]))
            # remember it is undirected graph
            d[edges[i][1]].append((edges[i][0], succProb[i]))

        # max probablity initially (-ve as we are using min heap)
        heap = [(-1.0, start, -1)]
        visited = set()

        while(heap):
            # we are inserting par bec we want to avoid insertion of par again
            p, src, par = heappop(heap)

            if src in visited:
                continue

            if(src == end):
                # we need to return inverse of p bec we are inserting -ve val of prob in heap
                return -p

            # visited will avoid any cycle
            visited.add(src)

            for dest, prob in d[src]:
                if(dest not in visited and dest != par):
                    # probability gets multiply
                    heappush(heap, (p*prob, dest, src))

        # in case we cant reach destination we will return 0
        return 0
