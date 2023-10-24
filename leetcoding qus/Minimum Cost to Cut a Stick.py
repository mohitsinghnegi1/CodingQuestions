import sys


class Solution(object):
    def minCost(self, n, cuts):
        """
        :type n: int
        :type cuts: List[int]
        :rtype: int
        """

        #         cuts.sort()

        #         dp = {}

        #         # instread off passing x and y , we can simply try to ut at all possible position that lises bettween i,j , ignore which does not lies inside .as number of cuts is 100 max
        #         def minCost(i,j,x,y):

        #             # cuts = cuts1[x:y]
        #             # print i,j,x,y

        #             if(x>=y): # make sure if there is no cut that means no cost
        #                 return 0

        #             if(i>=j):
        #                 return 0

        #             if(dp.get((i,j,x,y),None)!=None):
        #                 return dp[(i,j,x,y)]

        #             min_cost = sys.maxsize

        #             for k in range(x,y):
        #                 cost =  minCost(i,cuts[k],x,k) + (j-i) + minCost(cuts[k],j,k+1,y)
        #                 # print cost
        #                 min_cost = min(min_cost, cost)

        #             dp[(i,j,x,y)] =  min_cost
        #             return dp[(i,j,x,y)]

        #         return minCost(0,n,0,len(cuts))

        dp = {}

        # instread off passing x and y , we can simply try to ut at all possible position that lises bettween i,j , ignore which does not lies inside .as number of cuts is 100 max

        #         def minCost(i,j):

        #             # cuts = cuts1[x:y]
        #             # print i,j,x,y

        #             if(j-i==1):
        #                 return 0

        #             if(dp.get((i,j),None)!=None):
        #                 return dp[(i,j)]

        #             min_cost = sys.maxsize

        #             for k in range(len(cuts)):
        #                 if(i<cuts[k]<j):
        #                     cost =  minCost(i,cuts[k]) + (j-i) + minCost(cuts[k],j)
        #                     # print cost
        #                     min_cost = min(min_cost, cost)

        #             if(min_cost==sys.maxsize):
        #                 dp[(i,j)] = 0
        #             else:
        #                 dp[(i,j)] =  min_cost
        #             return dp[(i,j)]

        #         return minCost(0,n)

        """
        convert to dp

        j>i



        """
        dp = [[0] * (n + 1) for i in range(n + 1)]

        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n + 1):
                min_cost = sys.maxsize

                for k in range(len(cuts)):
                    if (i < cuts[k] < j):
                        cost = dp[i][cuts[k]] + (j - i) + dp[cuts[k]][j]
                        # print cost
                        min_cost = min(min_cost, cost)

                if (min_cost == sys.maxsize):
                    dp[i][j] = 0
                else:
                    dp[i][j] = min_cost

        # print dp
        return dp[0][n]




