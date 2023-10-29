# Qus:https://leetcode.com/problems/is-graph-bipartite/

class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """

        color = {}

        def bfs(src):
            queue = [src]

            color[src] = 0

            while (queue):
                u = queue.pop(0)

                for v in graph[u]:

                    if (v not in color):
                        color[v] = ~color[u]
                        queue.append(v)
                    elif (color[v] != ~color[u]):
                        return False

            return True

        for u in range(len(graph)):
            if (u not in color):
                if (not bfs(u)):
                    return False

        return True


