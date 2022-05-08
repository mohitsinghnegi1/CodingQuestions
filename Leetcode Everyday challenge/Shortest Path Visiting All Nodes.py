# https://leetcode.com/problems/shortest-path-visiting-all-nodes/submissions/
# Resource :https://www.youtube.com/watch?v=1XkMFNvkouo
class Solution(object):
    def shortestPathLength(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: int
        """

        if(len(graph)<=1):
            return 0

        visited = set()
        queue = []

        final_state = (1<<len(graph))-1
        # print final_state


        for i in range(len(graph)):

            queue.append((i,1<<i))


        shotest_path_len = 0
        while(queue):

            n = len(queue)
            shotest_path_len+=1

            while(n):

                node,bitstate = queue.pop(0)

                for v in graph[node]:

                    newbitstate = bitstate | 1<<v

                    if(final_state==newbitstate):
                        return shotest_path_len

                    if((v,newbitstate) not in visited):

                        queue.append((v,newbitstate))
                        visited.add((v,newbitstate))

                n-=1

        return -1
