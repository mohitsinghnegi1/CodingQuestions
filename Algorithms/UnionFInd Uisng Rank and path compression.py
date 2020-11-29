# Qus:https://leetcode.com/problems/redundant-connection/
class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """

        """
            Union Find Use Case
            Used to find the cycles in the graph
            Used to find the number of connected components
            TIme complexity O(N) using path compression
        """
        def find(a, x):

            par = a[x]
            while(par >= 0):
                x = par
                par = a[par]
            return x

        n = len(edges)
        a = [-1 for i in range(n+1)]

        for u, v in edges:
            parentU = find(a, u)
            parentV = find(a, v)

            if(parentU == parentV):
                return [u, v]

            # union(a,u,v)
            if(abs(a[parentU]) > abs(a[parentV])):
                # notice V have more node so v will be the parent
                # path compression
                a[u] = parentV
                a[parentU] = parentV
            else:
                # path compression
                a[v] = parentU
                a[parentV] = parentU
