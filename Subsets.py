# Qus:https://leetcode.com/problems/subsets/

def solve(nums,out,a=[],i=0):
    if(i>=len(nums)):
        out.append(a)
        return
        
    #dont take current element
    solve(nums,out,a,i+1)
    
    #take current element
    solve(nums,out,a+[nums[i]],i+1)
    
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        out=[]
        solve(nums,out)
        return out