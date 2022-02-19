# Qus:https://leetcode.com/problems/min-cost-to-connect-all-points/
from heapq import heapify, heappop, heappush
from collections import defaultdict
import sys
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


# 2nd time using kruskal algorithm


def find(par, u):

    while(par[u] > 0):
        u = par[u]
    return u


def findMSTCostUsingKruskalAlgo(lists, edges):
    # we will use krushkal algorithm to find

    lists.sort(reverse=True)

    addedEdges = 0
    totalCost = 0

    par = [-1]*(edges+1)

    while(addedEdges != edges):
        w, u, v = lists.pop()

        paruIdx, parvIdx = find(par, u), find(par, v)

        if(paruIdx != parvIdx):

            par[paruIdx] = parvIdx

            totalCost += w
            addedEdges += 1

    return totalCost


def constructGraph(points):
    graph = defaultdict(list)
    lists = []
    for u in range(len(points)):
        for v in range(u+1, len(points)):

            x1, y1 = points[u]
            x2, y2 = points[v]
            weight = abs(x2-x1)+abs(y2-y1)
            graph[u].append([v, weight])
            lists.append((weight, u, v))

    return graph, lists


class Solution2(object):
    def minCostConnectPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        graph, lists = constructGraph(points)
        # print graph
        # u ->(v,w) # its a dense graph each point connects to every other points

        cost = findMSTCostUsingKruskalAlgo(lists, len(points)-1)

        return cost
