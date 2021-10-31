# Qus:https://www.interviewbit.com/problems/delete-edge/#

# time complexity O(n)

"""
Intiution :
    find the sum of current sub tree , find the product of two sub tree using formula currentSubtreeSum * (total - currentSubtreeSum)
    return the max product

"""


from collections import defaultdict
class Solution:
    # @param A : list of integers
    # @param B : list of list of integers
    # @return an integer
    def __init__(self):
        self.ans = 0


    def getMaxProduct(self,weight, graph,total,u,par,MOD):

        sum1 = weight[u]

        for v in graph[u]:
            if(v!=par):
                ttl = self.getMaxProduct(weight, graph,total,v,u,MOD)
                sum1 += ttl
                # subtreeSum = weight[u] + ttl
                # self.ans = max(self.ans, ((total - subtreeSum) * subtreeSum))

        self.ans = max(self.ans, ((total - sum1) * sum1)%MOD)
        return sum1


    def deleteEdge(self, weight, edges):
        self.ans = 0
        MOD = 10**9 + 7
        graph = defaultdict(list)

        for u,v in edges:
            graph[u-1].append(v-1)
            graph[v-1].append(u-1)

        # print(weight)



        total = sum(weight)
        # print("total sum",total)

        maxProduct = self.getMaxProduct(weight, graph,total,0,-1,MOD)


        return self.ans
        # return 0

