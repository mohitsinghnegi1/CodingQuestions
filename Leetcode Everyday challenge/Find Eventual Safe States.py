# https://leetcode.com/problems/find-eventual-safe-states/solution/
class Solution(object):
    def eventualSafeNodes(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """
        # find all the nodes whose outdegree is 0
        # remove all these node , do the same process until there are no nodes remaining with outdegree zero



        # outdegree[u] -> count
        # indegree[v] -> list of parents


        # this was similar to topological sort

        outdegree = {}
        indegree = {}

        for v in range(len(graph)):
            indegree[v]  = set()


        for u in range(len(graph)):

            outdegree[u] = len(graph[u])


            for v in graph[u]:
                indegree[v].add(u)

        # print indegree, outdegree


        stack = []

        def zero_outdegree(stack,outdegree):
            for i in outdegree.keys():

                if(outdegree[i]==0):
                    stack.append(i)
                    del outdegree[i]

        def reduce_outdegree(nodes):

            for node in nodes:
                outdegree[node]-=1

                if(outdegree[node]==0):
                    stack.append(node)
                    del outdegree[node]




        zero_outdegree(stack,outdegree)

        isSafe = [False]*len(graph)
        while(stack):

            v = stack.pop()
            isSafe[v] = True
            nodes = indegree[v]
            reduce_outdegree(nodes)


        ans = []

        for i in range(len(graph)):
            if(isSafe[i]):
                ans.append(i)

        return ans














