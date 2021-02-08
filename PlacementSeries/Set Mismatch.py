# Qus:https://leetcode.com/problems/set-mismatch/
# using xor O(n) O(1) solution

class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        """
            for number 1 to n do xor with that nums val : you will get a^b
            
            we know 0^0 =0 and we also know both are different number there will be at least one 1
            
            so we will divide the array in two buckets based on first set bit
            How to find a first set bit ?  using xor & ~(xor - 1)
            
            2 bucket 
            
            bucket 1    bucket 2
            
        """
        n = len(nums)

        xor = 0
        for i in range(1, n+1):
            xor ^= (nums[i-1] ^ i)

        # print xor

        rsetbit = xor & ~(xor-1)
        # print rsetbit

        bucket1 = 0
        bucket2 = 0

        for i in range(1, n+1):

            if(i & rsetbit != 0):
                bucket1 ^= i
            else:
                bucket2 ^= i

            if(nums[i-1] & rsetbit != 0):
                bucket1 ^= nums[i-1]
            else:
                bucket2 ^= nums[i-1]

        c = nums.count(bucket2)
        if(c == 2):
            return [bucket2, bucket1]
        else:
            return [bucket1, bucket2]


# using math
class Solution2(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        d = {}
        for i in nums:
            if(i in d):
                dublicate = i
                break
            d[i] = True

        missing = n*(n+1)/2-sum(nums)+dublicate

        return [dublicate, missing]
