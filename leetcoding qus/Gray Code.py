# QUs:https://leetcode.com/problems/gray-code/

# TIme complexity : O(2**16)  ~ n**2 i think


class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        # see this image : search grey code image
        """
            Intution : for i = 1 we have grey code ['0','1']
                    for i =2 : ['0','1']+['1'+'0'] do mirror of old combine it
                    declare limit which is power of i 2**i : 2**2 , 2**3 ...
                    
                    for half of limit add 0 in either side (only matter is 1 digit change)
                    for more than half add 1 in either side of s[j]
                    
        
        """

        i = 1  # for i =1   limit = 2**i which is 2
        s = ['0', '1']  # i have difined grey code for 1 already bec
        # if i keep it empty , we can't multiply it by 2

        while(i < n):

            i += 1
            limit = 2**i  # dont forgot its power
            s += s[::-1]
            # print i,len(s),limit
            for j in range(limit/2):
                s[j] = s[j]+'0'  # Note: adding 0 or 1 in any side is valid
            for j in range(limit/2, limit):
                s[j] = s[j]+'1'
            # print s

        # at the end return the bin value of it
        return [int(val, 2) for val in s]


# efficient O(n) approach using bitwise operator
"""
    how to find the range : 1<<3 1 right shift by 3 which is equal to 8  Find range ==== > (1<<n)

    to calculate every element  of this range do xor of i with half of it     : i ^ (i>>1)

"""


class Solution2(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        result = []
        # left shift 1 by n places. for n =3 range will be 8
        return [i ^ (i >> 1) for i in range(1 << n)]
