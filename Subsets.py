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


# iterative method to find all subset using bit manipuation vvv imp

"""
    Intution : we know there are total 2*n-1 number of subset
    so we need to treverse from 1 to 2n-1 and for every i we need to pick only those element in array where the jth bit of ith elemetn is set
"""


class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        res = []

        # there are total 2**(n-1) number of subset
        for bi in range(2**(n)):

            ss = []
            for i in range(len(nums)):  # len bit in binary

                if(bi & 1 << i):
                    # if ith bit is one then we need to take it else not
                    ss.append(nums[i])
            # print ss
            res.append(ss)
        return res
