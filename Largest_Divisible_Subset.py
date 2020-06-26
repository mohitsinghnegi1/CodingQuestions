class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if(len(nums)<2):
            return nums
        
        nums.sort()
        
        dp=[1]*len(nums)
        
        max_index=0
        #create a dp array
        #see video https://www.youtube.com/watch?v=Wv6DlL0Sawg
        #time complexty n^2
        for i in range(len(nums)):
            for j in range(i):
                if(nums[i]%nums[j]==0):
                    if(dp[i]<dp[j]+1):
                        dp[i]=dp[j]+1
                        if(dp[i]>dp[max_index]):
                            max_index=i
        
        prevVal=nums[max_index]
        maxVal=dp[max_index]

                    
        out=[]    
        #now add the LCS such that all element of a subset divided by its previous element
        for i in range(len(nums)-1,-1,-1):
            if(prevVal%nums[i]==0 and dp[i]==maxVal):
                out.append(nums[i])
                maxVal-=1
                prevVal=nums[i]
        
        return out
            
                
                    
                    