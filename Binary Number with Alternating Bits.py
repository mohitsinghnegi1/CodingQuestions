# Qus:https://leetcode.com/problems/binary-number-with-alternating-bits/

class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        bit = n&1
        
        i=0
        while(n):
            # print "=>",bit
            # print "--",n&1
            if(bit!=n&1):
                return False
            bit = (bit+1)%2
            n = n>>1
        
            i+=1
        return True
        
        