# Qus:https://leetcode.com/problems/cheapest-flights-within-k-stops/


# solution TLE using recursion

from heapq import heappush, heappop, heapify
from collections import defaultdict
import sys


class Solution(object):
    def __init__(self):
        self.minCost = sys.maxsize

    def findCheapestPrice(self, n, flights, src, dst, K):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type K: int
        :rtype: int
        """
        # we are setting max because we need to find min dist
        self.minCost = sys.maxsize

        # we are using default dict bec we need default value to be set initially
        d = defaultdict(list)

        # create a dict that will store key as src and value as pair of dest and cost to reach
        # there
        for sc, dest, cost in flights:
            d[sc].append((dest, cost))

        def setCheapestPathCost(src, dst, cst, k):
            # number of stops should not be greater then K+1
            if(k > K+1):
                return
            # In case we are within max number of stops limit
            # we can update the global minCost
            if(src == dst):
                #print cst
                self.minCost = min(self.minCost, cst)
                return

            # we can still not reach the dest node
            # so traverse through its child node and see if you get the dest
            for dest, c in d[src]:
                setCheapestPathCost(dest, dst, cst+c, k+1)

        # this function will update gloabl minCost
        # it is taking src and dst as an arg so that we can keep track of cur node by using src val
        # cst will be the cst to reach that node from given source node
        # k denotes number of stops
        setCheapestPathCost(src, dst, cst=0, k=0)

        # if there are no solution return -1 else return minCost
        return self.minCost if self.minCost != sys.maxsize else -1


# optimised solution


class Solution1(object):
    def findCheapestPrice(self, n, flights, src, dst, K):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type K: int
        :rtype: int
        """
        # Modified Prime algorithm
        """
        Just use primes algorithm with an extra parameter of K 
        so we will not take that solutiomn which have K greater 
        
        # Point to Note: kushkal or primes is nothing but a bfs using heap instead of queue
        
        Time complexity O(ElogV + VlogV)
        we are adding each edges  O(E) also we are using heap which require logV as we are poping           the vertex
        """

        d = defaultdict(list)

        # construct a graph
        for s, ds, c in flights:
            # d -> destination. c - > cost to reach form s -> source
            d[s].append((ds, c))

        # heap state    cost,K(remaining stops),curNode
        heap = [(0, K, src)]

        while(heap):

            cost, remainingStops, src = heappop(heap)

            if(remainingStops < -1):
                # this is not a vailid bec stops should be less then K
                continue
            if(src == dst):
                # as soon as we reach to dst we will return as we know
                # there is no other minCost less then this possible (with no -ve weight)
                return cost

            # else add the adj nodes

            for ds, c in d[src]:
                # we need to add the cost and reduce the number of stops as well

                heappush(heap, (cost+c, remainingStops-1, ds))

        # in case there is no possible minimum path we will return -1
        return -1
