# Qus: https: // leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # do binary search

        l = 0
        h = len(nums)-1

        while(l <= h):
            mid = (h+l)/2

            if(nums[mid] > nums[h]):
                l = mid+1
            elif(nums[mid] < nums[h]):
                h = mid
            else:
                # if both equal
                if(h != 0 and nums[h-1] <= nums[h]):
                    h -= 1
                else:
                    return nums[h]
        return nums[h]
