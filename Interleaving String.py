# Qus: https://leetcode.com/problems/interleaving-string/

# 2**(len(s1)+len(s2)) time complexity


def solve(s1,s2,s3,i,j,k):
    
    if(k==len(s3) and j==len(s2) and i==len(s1)):
        return True
    
    
    if(i>=len(s1) and j>=len(s2)):
        return False
    
    first = second = False
    if(i<len(s1) and s1[i]==s3[k]):
        first =  solve(s1,s2,s3,i+1,j,k+1)
    if(j<len(s2) and s2[j]==s3[k]):
        second =  solve(s1,s2,s3,i,j+1,k+1)
    
    return first or second
    
class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if(len(s3)!=len(s1)+len(s2)):
            return False
        
        return solve(s1,s2,s3,0,0,0)


# optimise using memorization
def solve(s1,s2,s3,i,j,k,d):
    
    if(k==len(s3) and j==len(s2) and i==len(s1)):
        d[(i,j,k)] = True
        return d[(i,j,k)]
    if(d.get((i,j,k),False)!=False):
        return d[(i,j,k)]
    
    if(i>=len(s1) and j>=len(s2)):
        return False
    
    first = second = False
    if(i<len(s1) and s1[i]==s3[k]):
        first =  solve(s1,s2,s3,i+1,j,k+1,d)
    if(j<len(s2) and s2[j]==s3[k]):
        second =  solve(s1,s2,s3,i,j+1,k+1,d)
        
    d[(i,j,k)] = first or second
    
    return d[(i,j,k)]


"""
    2 pass
    
    dp[i][j][k] = dp[i+1][j][k+1] or dp[i][j+1][k+1]
    
    
    or 
    dp[i][k] = dp[i+1][k+1]
    
    or 
    dp[j][k] = dp[j+1][k+1]

    Base dp[0][0] = 0
    dp
"""
class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if(len(s3)!=len(s1)+len(s2)):
            return False
        
        d = {}
        return solve(s1,s2,s3,0,0,0,d)