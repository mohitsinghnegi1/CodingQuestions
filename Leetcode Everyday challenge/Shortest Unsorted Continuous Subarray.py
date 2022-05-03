class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        TIme complexity : O(n)
        Space complexity : o(n)

        Intution : 1. find the left most place where the max till current element from the begining is greter then the
        min of element henceforth

        2. find the right most place where the min till current element from the last is smaller then the
        max of elements before current element from the begining

        return the difference , in case no such indexs exist return 0


        """



        p = [0]*len(nums)
        p[0] = nums[0]

        s = [0]*len(nums)
        s[-1] = nums[-1]


        for i in range(1,len(nums)):
            p[i] = max(p[i-1],nums[i])

        for i in range(len(nums)-2,-1,-1):
            s[i] = min(s[i+1],nums[i])


        minI = len(nums)
        maxI = -1


        for i in range(len(nums)-1):

            if(p[i]>s[i+1]):
                minI = i
                break

        for i in range(len(nums)-1,-1,-1):

            if(p[i-1]>s[i]):
                maxI = i
                break

        return maxI - minI + 1 if minI!=len(nums) else 0;



