# https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/
from collections import defaultdict
class Solution(object):
    def minReorder(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """
        """
        Intution : consider this as a undirected graph
        u -> v false
        v - > u true # here true denotes that we have to rotate the edges


        """


        graph = defaultdict(list)
        visited = [False]*n

        for u,v in connections:
            graph[u].append((v,1))
            graph[v].append((u,0))


        def dfs(u):

            visited[u] = True

            count = 0
            for v,need_rotation in graph[u]:


                if(visited[v]==False):
                    count += need_rotation + dfs(v)

            return count



        count = dfs(0)

        return count