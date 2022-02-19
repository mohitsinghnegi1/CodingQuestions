# Qus:https://leetcode.com/problems/single-number-iii/

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        xor = 0
        for i in nums:
            xor = xor^i
        # print xor # this is xor of 2 single number 
        # now we need to find these two number
        no = 1
        while(xor&no!=no):
            # print xor&1
            no = no<<1
        # print no
        
        
        xor1 = 0
        xor2 = 0
        
        # since one number is in one bucket and another in another bucket
        
        for val in nums:
            if(val&no==no):
                xor1^=val
            else:
                xor2^=val
        return [xor1,xor2]
            
        
        
        
        
        
        
        
        
        
        
        
        
        
            