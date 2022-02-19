# Qus:https://leetcode.com/problems/subsets-ii/

from collections import defaultdict


class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        """
            Remember subset is not contigious
            Subset order does not matters ie (1,2,3) is same as (3,2,1)
            dict can store tuple and avoid dublicates (list can 't be put as a key)
        """

        d = defaultdict(int)
        out = []

        def getSubset(nums, i, ans=()):

            if(i == len(nums)):
                d[tuple(sorted(ans))] += 1
                return
            # include
            getSubset(nums, i+1, ans=ans+(nums[i],))
            # exclude
            getSubset(nums, i+1, ans)

        getSubset(nums, 0)
        out.extend(d.keys())
        return out


class Solution2(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        """
            Intution : First code to generate all possible subsets 
            ie ( out=[[]] , for every new element we combine it with all the previous 
            elements that we have already inserted )  --
            although this will not handle dublicate but this will be good enough 
            to procceed with the next step
            the problem here is that we dont want to include the elemtn that was before
            dublicate element (1,2,2) like in this case we have out state as [[] [1]] 
            before adding new subsets we need to store the len of out in l so that 
            dublicate element (2) dont use elemnts before that len (which is 2)
            hence it will avoid those 
        
        """

        # sort the nums in order to avoid dublicates
        nums.sort()
        out = [[]]

        for i in range(len(nums)):

            if(i == 0 or nums[i] != nums[i-1]):
                l = len(out)
            n = len(out)
            for j in range(n-l, n):
                out.append(out[j]+[nums[i]])
        return out
