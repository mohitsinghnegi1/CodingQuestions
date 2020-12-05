# Qus:https://leetcode.com/problems/min-cost-to-connect-all-points/
from heapq import heappush, heappop


def constructHeap(points):
    n = len(points)
    heap = []
    # calculate mahantaa distance between all nodes
    for i in range(n):
        for j in range(i+1, n):
            if(i != j):
                dist = abs(points[i][0]-points[j][0]) + \
                    abs(points[i][1]-points[j][1])
                # w[i][j]=dist
                # push by weight
                heappush(heap, [dist, i, j])
    return heap


class Solution(object):
    def minCostConnectPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        """
        Intution :
        1.First find the weight between each points 
        2.Calculate and insert the weight + index of sorce point and index of destination point
        3.Pop out min weight elemnt from the heap and check if they are not forming any cycle
        4.if they are not forming cycle then do union of these two point and add weight to                   totalWeight
        
        """

        n = len(points)
        # this will return a heap which will return us min weighted node
        heap = constructHeap(points)

        # print heap
        # a min spanning tree consists of n-1 nodes and have the minimum weight

        par = [-1]*len(points)

        def find(u):
            while(par[u] >= 0):
                u = par[u]
            return u

        numberOfAddedEdges = 0
        totalWeight = 0

        while(numberOfAddedEdges < n and heap != []):

            # i and j denoting index of points it means
            # mahanta distance between points[i] and points[j] is weight
            weight, u, v = heappop(heap)

            parU = find(u)
            parV = find(v)

            if(parU != parV):
                # then this edge is contibute to the totalWeight
                totalWeight += weight

                # do union (You can do optimisation like path compression or  ranking)
                par[parV] = parU
                par[v] = parU
                numberOfAddedEdges += 1

        return totalWeight
