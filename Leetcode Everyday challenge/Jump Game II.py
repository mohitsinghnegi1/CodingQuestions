# Qus:https://leetcode.com/problems/jump-game-ii/

# dp O(N**2) solution
import sys
class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        time complexity O(N**2)
        # dp[i] = how many just it requires to reach to this index
        dp=[sys.maxsize]*len(nums)
        dp[0]=0
        for i in range(1,len(nums)):
            for j in range(i):
                if(j+nums[j]>=i):
                    dp[i] = min(dp[i],dp[j]+1)
        return dp[-1]


# O(N) solution 
    
class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if(n==1):
            return 0
        
        count = 1
        cur = nums[0] # 1
        lastIdx = nums[0]  # 1
        if(cur>=n-1):
            return count
        
        for i in range(1,n): # 1 2
            lastIdx = max(lastIdx,i+nums[i])  # 3 3
            if(i>=cur): # true
                # change the ladder
                count += 1 # 2
                cur = lastIdx # 3
                if(cur>=n-1): # false
                    return count
                
        return count
            
            
            
            
            
    
        