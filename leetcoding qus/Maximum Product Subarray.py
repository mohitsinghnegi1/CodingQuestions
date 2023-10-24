# Qus:https://leetcode.com/problems/maximum-product-subarray/

import sys
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        """

        # Kadans algorithm modification
        # https://leetcode.com/problems/maximum-product-subarray/discuss/48230/Possibly-simplest-solution-with-O(n)-time-complexity
        n = len(nums)
        maxi = nums[0]  # stores max product finishes at i (this will always store max product)
        mini = nums[0]  # stores min product so far till i
        max_so_far = nums[0]

        for i in range(1,n):

            if(nums[i]<0):
                mini,maxi = maxi,mini # swap since -ve value will convert max to min and min to max
                mini = mini*nums[i]
                maxi = maxi*nums[i]


            if(nums[i]==0): # both will be turn zero
                maxi = 0
                mini = 0


            if(nums[i]>0):
                maxi = maxi*nums[i] # positive will remain positive so no change in maxi and mini
                mini = mini*nums[i] # -ve will remain -ve

            maxi = max(maxi,nums[i])
            mini = min(mini,nums[i])

            max_so_far = max(maxi,max_so_far)

        return max_so_far

        # striver approach

        """
        Four case : 
        
        1. All positive : complete array product should be the answer
        2. Even number of -ve : complete array product should be the answer
        3. Odd number of -ve: except one odd max(prefix, suffix) would be the answer
        4. if any zero : zero would break the subarray , as we don't want to include it in product of next sub array, so set it to pref = 1 if pref comes out to be zero
        Time complixity : O(n) , Space complexity : O(1)
        
        
        """

        """
        n = len(nums)
        
        pref = 1
        suf = 1
        max_so_far = -sys.maxsize
        for i in range(n):
            
            pref = pref*nums[i]
            suf = suf*nums[n-i-1]
            
            max_so_far = max(pref,suf,max_so_far)
            
            if(pref==0):
                pref = 1
            if(suf==0):
                suf = 1
        
        return max_so_far
        
        """

        """
        n = len(nums)
        dp = {}
        
        def solve(i,prevProduct):
            
            if(i>=n):
                return prevProduct
            
            if(dp.get((i,prevProduct),None)!=None):
                return dp[(i,prevProduct)]
            
            # is current element part of subarray
            
            part = solve(i+1,prevProduct* nums[i])
            # print part
            notPart = solve(i+1,nums[i])
            # print notPart
            
            dp[(i,prevProduct)] = max(part,notPart,prevProduct* nums[i],nums[i]) # include part , and notpart as well to consider max out of all possible subarrays
            return dp[(i,prevProduct)]
            
            
        return solve(0,1)
        
        """

















