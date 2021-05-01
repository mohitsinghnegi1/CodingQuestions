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


# easy to understand using binary search
def binarySearch(nums, target):

    l = 0
    r = len(nums)

    while(l < r):
        mid = (l+r)/2

        if(nums[mid] == target):
            return mid
        elif(target < nums[mid]):
            r = mid
        else:
            l = mid + 1
    return -1


def findPivot(nums):

    l = 0
    r = len(nums)

    while(l < r):
        mid = (l+r)/2

        if(nums[mid] >= nums[0]):  # = bec [3,1]   3

            if(nums[mid+1] < nums[mid]):
                return mid+1
            l = mid+1
        else:
            r = mid
    return l


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        if(len(nums) < 1):
            return -1

        if(nums[0] <= nums[-1]):
            return binarySearch(nums, target)

        pivot = findPivot(nums)
        print "pivot ", pivot

        if(target > nums[-1]):
            # search in left side
            return binarySearch(nums[:pivot], target)

        else:
            # search in right side
            index = binarySearch(nums[pivot:], target)
            return -1 if(index == -1) else pivot + index  # add pivot index
            # Remember in case elemnt not found then return -1
