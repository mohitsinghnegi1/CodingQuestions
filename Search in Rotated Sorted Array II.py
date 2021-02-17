# Qus:https://leetcode.com/problems/search-in-rotated-sorted-array-ii/

def findPivotIndex(nums):
    l = 0
    r = len(nums)-1

    while(l < r):
        mid = (l + r)/2

        if(nums[mid] < nums[r]):
            r = mid

        elif(nums[mid] > nums[r]):

            l = mid+1

        else:
            # if both are equal
            if(r != 0 and nums[r-1] <= nums[r]):
                r -= 1
            else:
                return r

    return r


def binarySearch(nums, l, r, target):

    while(l < r):
        mid = (l+r)/2
        if(nums[mid] == target):
            return True
        elif(target < nums[mid]):
            r = mid
        else:
            l = mid+1

    return False


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        # worse time complexity O(n) if duplicate and averge case O(logn) if no duplicate
        # first find pivot index
        pindex = findPivotIndex(nums)

        r = len(nums)

        # then perform simple binary seearch in one of two divided sorted array
        # based on condition below
        if(target < nums[r-1]):
            return binarySearch(nums, pindex, r, target)
        elif(target > nums[r-1]):
            return binarySearch(nums, 0, pindex, target)
        else:
            return True
