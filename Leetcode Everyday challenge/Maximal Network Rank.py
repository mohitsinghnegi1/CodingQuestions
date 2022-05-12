# Qus: https://leetcode.com/problems/maximal-network-rank/
# time complexity O(N**2)
class Solution(object):
    def maximalNetworkRank(self, n, roads):
        """
        :type n: int
        :type roads: List[List[int]]
        :rtype: int
        """

        graph = {}

        for i in range(n):
            graph[i] = set()


        for u,v in roads:

            graph[u].add(v)
            graph[v].add(u)



        ans = 0


        for u in graph:

            for v in graph:

                if(u!=v):
                    # print u,v,len(graph[u]) + len(graph[v])
                    count = len(graph[u]) + len(graph[v])

                    if(v in graph[u]):
                        count -= 1 # remove the common edge if exist between two nodes

                    ans = max(ans,count)
        return ans