# Qus:https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

import bisect


class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if(not len(nums)):
            return [-1, -1]

        a = bisect.bisect_left(nums, target)
        b = bisect.bisect_right(nums, target)

        if(a < len(nums) and nums[a] != target):
            return [-1, -1]
        if(a == len(nums)):
            return [-1, -1]

        return [a, b-1 if b != -1 else -1]
