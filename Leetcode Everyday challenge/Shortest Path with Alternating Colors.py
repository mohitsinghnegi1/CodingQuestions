# https://leetcode.com/problems/shortest-path-with-alternating-colors/
from collections import defaultdict
import sys
class Solution(object):
    def shortestAlternatingPaths(self, n, redEdges, blueEdges):
        """
        :type n: int
        :type redEdges: List[List[int]]
        :type blueEdges: List[List[int]]
        :rtype: List[int]
        """

        dist1 = [sys.maxsize]*n
        dist2 = [sys.maxsize]*n

        redgraph = defaultdict(list)
        bluegraph = defaultdict(list)

        for u,v in redEdges:
            redgraph[u].append(v)

        for u,v in blueEdges:
            bluegraph[u].append(v)

        # red = 0 , blue =1

        def dfs(u,color,d):

            dist = dist2 if color else dist1

            """
            Ex Case : 5
            [[0,1],[1,2],[2,3],[3,4]]
            [[1,2],[2,3],[3,1]]
            Note: we also need to take the visited & graph or dist based on the color

            We should allow visiting the same node with red & blue clour both ,
            In case one visited the same node with same color then we should not allow it
            """

            if(dist[u]<=d):
                return
            dist[u] = d

            for v in bluegraph[u] if color else redgraph[u]:
                dfs(v,(color+1)%2,d+1)






        dfs(0,0,0)
        dfs(0,1,0)

        # print dist1
        # print dist2


        ans = []

        for i,j in zip(dist1,dist2):

            min1 = min(i,j)

            ans.append(min1 if min1!=sys.maxsize else -1)

        return ans






