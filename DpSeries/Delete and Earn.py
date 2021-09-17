# Qus:https://leetcode.com/problems/delete-and-earn/

def robMax(houses):
    
    if(len(houses)==1):
        return houses[0]
    if(len(houses)==2):
        return max(houses)
    
    dp = [0]*(len(houses))
    # dp[i] is max profit if you rob houses up to i index you can either rob the ith house or not
    dp[0] = houses[0]
    dp[1] = max(houses[:2])
    
    for i in range(1,len(houses)):
        
        dp[i] = max(dp[i-1],dp[i-2]+houses[i])
    
    return dp[-1]
    
    
    
class Solution(object):
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # this problem is similar to house robber 1 problem 
        # where you can't rob adjecent house
        
        houses = [0]* (max(nums)+1)
        
        for i in nums:
            houses[i] += i
        
        return robMax(houses)