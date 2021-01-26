# Qus:https://leetcode.com/problems/subsets/

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        out = []

        def getAllSubset(nums, i=0, subset=[]):

            if(i >= len(nums)):
                out.append(subset)
                return

            getAllSubset(nums, i+1, subset+[nums[i]])
            getAllSubset(nums, i+1, subset)

        getAllSubset(nums)
        return out
