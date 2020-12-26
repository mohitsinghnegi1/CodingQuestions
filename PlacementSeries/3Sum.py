# Qus:https://leetcode.com/problems/3sum/

# time complexity O(n**2)

"""
    Intution :
        sort the array
        set one index as a first ele of triplet

        then do two pointer approach : move j pointer to right if we need more , else dec k if we want to reduce cur sum

"""


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)

        if(n < 3):
            return []

        nums.sort()

        out = []
        i = 0
        while(i < n-2):

            # to make the sum zero , we need to get target opposite to cur val ie nums[i]
            target = -(nums[i])

            # performn two pointer approach
            j = i+1
            k = n-1
            while(j < k):

                curSum = nums[j]+nums[k]

                if(target == curSum):
                    out.append([nums[i], nums[j], nums[k]])

                    # increment j until it is not equal to previous element
                    j += 1
                    while(j < k and nums[j] == nums[j-1]):
                        j += 1

                elif(curSum < target):
                    j += 1
                else:
                    k -= 1

            # increment i until value at i index is not equal to previous element
            i += 1
            while(i < n-2 and nums[i] == nums[i-1]):
                i += 1
        return out
