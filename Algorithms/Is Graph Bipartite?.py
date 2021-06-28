# Qus:https://leetcode.com/problems/is-graph-bipartite/


def bfs(i, graph, color, n):

    c = 0
    queue = [i]

    while(queue):
        v = []
        while(queue):
            node = queue.pop()
            if(color[node] == -1):
                color[node] = c

                for i in graph[node]:
                    if(color[i] == -1):
                        v.append(i)

            elif(color[node] != c):

                return False
        queue = v
        c = 1 - c

    return True


class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """

        # bipertite graph is a graph have two colors
        # A biprtite graph does not contain odd length cycle

        n = len(graph)
        color = [-1]*n

        for i in range(n):
            if(color[i] == -1):
                # perform bfs on this component
                isBipertiteComponent = bfs(i, graph, color, n)

                if(not isBipertiteComponent):
                    # print(color)
                    return False
        return True
