# QUs: https: // leetcode.com/problems/redundant-connection-ii/

# Resource :https://www.youtube.com/watch?v=U7_ynlauYh0

# optimised solution using union find
# time complexity  O(edges*logn)~ O(edges*1) with path compression
class Solution(object):
    def findRedundantDirectedConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """

        # this will keep track of parent node
        par = [-1]*(len(edges)+1)

        def find(u):

            while(par[u] > 0):
                u = par[u]
            return u

        possibleEdge1 = None
        possibleEdge2 = None

        # find if there is the case of node have 2 parent
        for u, v in edges:
            if(par[v] != -1):
                possibleEdge1 = [par[v], v]
                possibleEdge2 = [u, v]
                # there is only one verted who might have two parent (including loop)
                """
                1 -> 2 <- 3.         ans remove 1-> 2 (3 -> 2 -> 1)     1-> 2 -> 1 will cause loop 
                | <- | 
                
                """
                break

            par[v] = u

        # print possibleEdge1,possibleEdge2
        # remember to reset the parent node
        par = [-1]*(len(edges)+1)

        for u, v in edges:

            # assume that we have removed one of the ans edge if exist
            if [u, v] == possibleEdge2:
                continue

            parU = find(u)
            parV = find(v)

            if(parU == parV):
                # if possible edge is still there then return it else return the last encountered                   # node
                # this is the case when we have removed the wrong edge or having a loop
                # A vertex has more than 1 parent, and is part of a loop.
                return possibleEdge1 if possibleEdge1 else [u, v]

            # do union by rank and compression
            if(par[parU] > par[parV]):

                par[parU] += par[parV]
                par[v] = parU
                par[parV] = parU

            else:
                par[parV] += par[parU]
                par[u] = parV
                par[parU] = parV

        # if tree has no loop then then our guess is right
        # possibleEdge2 is the added edge

        return possibleEdge2
