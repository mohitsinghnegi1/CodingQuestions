# Qus:https://leetcode.com/problems/combination-sum-iv/submissions/

#----------------------------------------#
#soltion using memorization giving tle
#----------------------------------------#

def solve(nums,target,ways):
    
    if(ways.get(target,False)):
        return ways[target]
    
    if(target==0):
        return 1
    if(target<0):
        return 0
    
    ans=0
    #else target greater then 0
    for i in nums:
        if(target-i>=0):
            ans+=solve(nums,target-i,ways)
        else:
            break
    
    ways[target]=ans
    return ways[target]


class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        ways={}
        #soting to fasten the process
        nums.sort()
        
        #this function will give number of combinations
        return solve(nums,target,ways)
        
        
        
#--------------------------------------------#   
# SOl 2 : optimal solution using dp
#--------------------------------------------#

class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        #similar to approach of bfs
        
        dp=[0]*(target+1)
        dp[0]=1

        #suppose i am at start_pos we can jum to any target using number in array it will add current 
        #ways to next target position as we know we come to last position using m ways then same way we can reach to next pos
        for start_pos in range(target):
            for jump in nums:
                if(start_pos+jump<=target):
                    dp[start_pos+jump]+=dp[start_pos]
            
        return dp[target]
            
        
        
        
        
