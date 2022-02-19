# qus:https://leetcode.com/problems/unique-paths/
# in python 3

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        @lru_cache
        def path(r, c, n, m):
            if(r == n or c == m):
                return 1

            a = path(r+1, c, n, m)
            b = path(r, c+1, n, m)

            return a+b

        # bottom up approach
        return path(1, 1, n, m)

# bottom up approach (2 time) >>>>>>>>


# sol 2 bottom up


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        # bottom up approach

        out = []
        for i in range(n):
            row = []
            for j in range(m):
                row.append(1)
            print(row)
            out.append(row)
        # print(out)
        for i in range(1, n):
            for j in range(1, m):
                out[i][j] = out[i-1][j]+out[i][j-1]
        # print(out)
        return out[-1][-1]

     # sol3 using bottom up
     class Solution:
        def uniquePaths(self,m:int,n:int)->int:
        
        # bottom up approach
        
        out=[]
        for i in range(m):
            v=[]
            for j in range(n):
                if(len(out)>0):
                    if(j>0):
                        v.append(out[i-1][j]+v[-1])
                    else:
                        v.append(1)
                else:
                    if(j>0):
                        v.append(v[-1])
                    else:
                        v.append(1)
            out.append(v)
            
        return(out[-1][-1])
                        
                
    # sol 4 using 1D  array O(n) space
    class Solution:
        def uniquePaths(self, m: int, n: int) -> int:
        dp = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                dp[j] = dp[j - 1] + dp[j]
        return dp[-1]        
                       
                
            
    
    
    
    
    


class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        d = {}

        def totalPath(n, m, i, j):

            if(i == 1 or j == 1):
                return 1

            if((i, j) in d):
                return d[(i, j)]
            ans = totalPath(n, m, i-1, j)+totalPath(n, m, i, j-1)
            d[(i, j)] = ans
            return d[(i, j)]

        return totalPath(n, m, n, m)
