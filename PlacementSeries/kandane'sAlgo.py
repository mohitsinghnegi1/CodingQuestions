# QUs : https://leetcode.com/problems/maximum-subarray/
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_so_far = nums[0]
        max1 = nums[0]
        for i in range(1, len(nums)):
            # if array contains only -ve numbers then largest number will be
            # the -ve number
            # so to handle that case we are use max1=max(nums,max1+nums[i])
            max1 = max(nums[i], max1+nums[i])
            max_so_far = max(max1, max_so_far)
        return max_so_far
