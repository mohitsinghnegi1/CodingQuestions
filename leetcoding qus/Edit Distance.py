import sys
class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        #         dp = {}

        #         def minOp(i,j):
        #             # what operation should i perform when i am at ith position

        #             if(j==len(word2)):
        #                 return len(word1)-i # in case j is over , then we need to delete remaining character in word1 , which will count as an operation **Note

        #             if(i>=len(word1)):
        #                 return len(word2)-j

        #             if(dp.get((i,j),None)!=None):
        #                 return dp[(i,j)]

        #             # if equal skip the operation
        #             equal = sys.maxsize
        #             if(i < len(word1) and word1[i]==word2[j]):
        #                 equal =  minOp(i+1,j+1)


        #             # replace only valid if i < n
        #             replace = sys.maxsize #  assign it max value otherwise it will not give correct result for some of the cases
        #             if(i < len(word1)):
        #                 replace = 1 + minOp(i+1,j+1)

        #             # delete
        #             delete = sys.maxsize  #  assign it max value otherwise it will not give correct result for some of the cases

        #             if(i<len(word1)):
        #                 delete = 1 + minOp(i+1,j)

        #             # insert
        #             insert = 1 + minOp(i,j+1)

        #             dp[(i,j)] =  min(replace,insert,delete,equal)
        #             return dp[(i,j)]


        #         return minOp(0,0)


        """
        Convert it into dp
        
        
        i = 0 to min(n,m)     
        j = 0 to min(n,m)
        
        
        dp[i][j+1]
        dp[i+1][j]
        dp[i+1][j+1]
        bottom right corner
        
        base values
        
        corner  = 0
        mth column = len(word1) - i
        nth colum = len(word2)-j
        
        i = n-1 to 0
        j = m-1 to 0

        result will be stored in dp[0][0]
        
        """
        n = len(word1)
        m = len(word2)

        dp = [[sys.maxsize]*(m+1) for i in range(n+1)]


        for i in range(n):
            dp[i][m] = len(word1) - i

        for j in range(m):
            dp[n][j] = len(word2) - j


        dp[n][m] = 0




        for i in range(n-1,-1,-1):
            for j in range(m-1,-1,-1):

                # if equal skip the operation
                equal = sys.maxsize
                if(word1[i]==word2[j]):
                    equal =  dp[i+1][j+1]

                # replace only valid if i < n
                replace = sys.maxsize #  assign it max value otherwise it will not give correct result for some of the cases
                if(i < len(word1)):
                    replace = 1 + dp[i+1][j+1]

                # delete
                delete = sys.maxsize  #  assign it max value otherwise it will not give correct result for some of the cases

                if(i<len(word1)):
                    delete = 1 + dp[i+1][j]

                # insert
                insert = 1 + dp[i][j+1]

                dp[i][j] =  min(replace,insert,delete,equal)

        return dp[0][0]



