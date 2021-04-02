# kruskal's algorithm is used to find minimum spanning tree - undirected , weighted graph

# kushkal is genrally applied on connected graph
# if kushkal is applied on disonnected graph then it will give minimum spanning tree of all disonnected components

from collections import defaultdict


class Graph(object):

    def __init__(self, v):
        self.graph = []  # this is a list where each index will contain a list in form [w,u,v]
        self.v = v

    def addEdge(self, u, v, w):
        self.graph.append([w, u, v])

    def krushkalMST(self):

        # to detect a cycle we need to use union find algorithm

        par = [-1]*self.v

        def find(u):

            while(par[u] > -1):
                u = par[u]
            return u

        # sort graph on the basis of weight bec we need to add minimum edge first in krushkal's algorithm if there is no cycle
        self.graph.sort(key=lambda x: x[0])

        for w, u, v in self.graph:

            paru = find(u)
            parv = find(v)

            if(paru != parv):
                #print par
                print u, " - ", w, " -> ", v

                # if parent are not same then perform union with path compression and ranking

                if(abs(par[paru]) > abs(par[parv])):
                    # add ranking
                    par[paru] += par[parv]
                    par[parv] = par[paru]
                    # note below statement par[v]=paru not par[v]=par[paru] otherwise it will give wrong ans
                    par[v] = paru

                else:
                    # add ranking
                    par[parv] += par[paru]
                    par[paru] = par[parv]
                    par[u] = parv
                    # add ranking


g = Graph(4)
g.addEdge(0, 1, 10)
g.addEdge(0, 2, 6)
g.addEdge(0, 3, 5)
g.addEdge(1, 3, 15)
g.addEdge(2, 3, 4)

g.krushkalMST()


# 2nd time revision
# Qus: https: // leetcode.com/problems/min-cost-to-connect-all-points/


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
