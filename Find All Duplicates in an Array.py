# Qus:https://leetcode.com/problems/find-all-duplicates-in-an-array/

class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        """
        Use cyclic solution 
        index to index val swapping until correct element comes to correct index
        if you are same i and same value then just move forward
        if the element you want to sswap is same as then element present at that index then
        it is dublicate
        at the end return the set 
        
        """

        def swap(i, j):
            nums[i], nums[j] = nums[j], nums[i]

        out = []
        i = 1
        nums = [0]+nums
        while(i < len(nums)):

            if(i != nums[i] and nums[nums[i]] == nums[i]):
                out.append(nums[i])
                i += 1
            elif(i == nums[i]):
                i += 1
            else:
                swap(i, nums[i])

        return list(set(out))
