# Qus:https://leetcode.com/problems/network-delay-time/

# coded by myself in 1st attempt , better quality then before

from collections import defaultdict
from heapq import heappop, heappush


class Solution(object):
    def networkDelayTime(self, times, N, src):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        """
        Here we will use dijkastra to find the shorted distance to all nodes
        
        
        
        """

        # construct a graph
        d = defaultdict(list)
        for u, v, w in times:
            d[u].append((v, w))

        # max time will keep track of max time taken to reach a specific node
        maxTime = 0
        # visited will avoid any cycle
        # as we know using heap once we reach a node the destance will be the minimum possible
        # distance so once we reach that node we will set the visited to true
        visited = set()
        # remember we will set the visited true after we pop out the node
        # bec (heap can return some other min path node )
        # we are sure that once heap pop the node it will be the min dist to reach that
        # node , but until it is not prove that this is the min dis we need to append the node

        heap = [(0, src)]

        while(heap):
            time, src = heappop(heap)
            # this condition is also important bec
            # there might be possible that heap have two same src node but one have less wight then
            # other (one souce is already inside visited)
            if(src in visited):
                continue
            maxTime = max(maxTime, time)
            visited.add(src)
            for dest, w in d[src]:

                # we know that , heap already given sortest distance to reach this node
                # so dont push it, push only those dest which path is not yet confirmed
                if(dest not in visited):
                    heappush(heap, (time+w, dest))

        return maxTime if len(visited) == N else -1
