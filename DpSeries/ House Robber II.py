# QUs:https://leetcode.com/problems/house-robber-ii/

def solve(nums):
    # print nums
    n = len(nums)
    
    if(n==0):
        return 0
    if(n==1):
        return nums[0]
    if(n==2):
        return max(nums)
    if(n<=3):
        return max(nums[0]+nums[2],nums[1])
    
    
    dp = [0]*(n+1)
    dp[0] = 0
    dp[1] = nums[0]
    dp[2]= max(nums[:2])
    dp[3]=max(nums[0]+nums[2],nums[1])
    
    for i in range(3,n+1):
        dp[i] = nums[i-1]+max(+dp[i-2],dp[i-3])
    # print dp
    return max(dp[-1],dp[-2])
    
    
def solution2(nums):
    n = len(nums)
    
    if(n==0):
        return 0
    if(n==1):
        return nums[0]
    
    dp = [0]*(n+1)
    dp[1] = nums[0]
    
    for i in range(2,n+1):
        # rob or dont rob
        dp[i] = max(dp[i-2]+nums[i-1],dp[i-1])
    
    return dp[-1]



class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        """
        Another intution will be to either rob a house or dont reb the house
        if you rob the house then dp[i] = nums[i] + dp[i-2]
        else dp[i] = dp[i-1]
        
        """

        if(len(nums)==1):
            return nums[0]
        
#         max1 = solve(nums[:-1]) # dont consider one element from end to avoid if you take first element
#         max2 = solve(nums[1:])  # dont consider first element is you take last one
        
        max1 = solution2(nums[:-1]) # dont consider one element from end to avoid if you take first element
        max2 = solution2(nums[1:])  # dont consider first element is you take last one
        
        return max(max1,max2) # one of them will give max ans