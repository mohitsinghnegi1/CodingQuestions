# Qus:https://leetcode.com/problems/wiggle-sort-ii/

class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # Timecompleixty : o(nlogn)
        # Space complexity : o(n)
        nums.sort()

        out = []
        mid = (len(nums)+1)/2  # seee the formula
        print nums

        l = nums[:mid][::-1]  # reverse left half
        r = nums[mid:][::-1]  # reverse right half after sorting

        # update array
        for i in range(len(nums)):
            if(i < mid):
                nums[i] = l[i]
            else:
                nums[i] = r[i-mid]

        print nums

        # construct result arr by adding greater element in the middle
        for i in range(0, len(nums)):
            if(i % 2 == 0):
                out.append(nums[i/2])
            else:

                out.append(nums[mid+i/2])

        for i in range(len(nums)):
            nums[i] = out[i]
