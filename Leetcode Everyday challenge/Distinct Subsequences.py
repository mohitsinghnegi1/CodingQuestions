# Qus:https://leetcode.com/problems/distinct-subsequences/
# brute force
def solve(s,t,i,j):
    if(j==len(t)):
        return 1
    if(i==len(s)):
        return 0
    
    if(s[i]!=t[j]):
        return solve(s,t,i+1,j)
    
    # we can either take and dont take
    take = solve(s,t,i+1,j+1)
    donttake = solve(s,t,i+1,j)
    
    return take+donttake

class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        return solve(s,t,0,0)


# conversion to bottom up approach 
# t[i]!=s[i] 
# then dp[i][j] = dp[i+1][j]

# t[i]==t[j]
# then dp[i][j] = dp[i+1][j+1]+dp[i+1][j]




# conversion to bottom up dp approach
# time complexity O(N**2)
class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        
        n = len(s)
        m = len(t)
        
        dp = [[0 for _ in range(m+1)] for i in range(n+1)]
        
        # make all the last col element one
        
        for i in range(n+1):
            dp[i][-1] = 1
            
        
        for i in range(n-1,-1,-1):
            for j in range(m-1,-1,-1):
                if(s[i]!=t[j]):
                    dp[i][j] = dp[i+1][j]
                else:
                    dp[i][j] = dp[i+1][j]+dp[i+1][j+1]
        # print dp
        return dp[0][0]
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        