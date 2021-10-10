# Qus:https://leetcode.com/problems/bitwise-and-of-numbers-range/

class Solution(object):
    def rangeBitwiseAnd(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        """
        Observations:
            1. if any of ith bit  flips from 0 to 1 or 1 to 0 the ans ith bit will be  0 . as we are finding and
            2. if we are adding a new bit then all the right hand side bit are already flipped
                For example 2 & 3.   1 1.    1 0 0

            3. <---m bit (fixed - left and right bit will be equal)-----><-----n bit (flipped)----->
            
            
        
        """
        
        leftB = bin(left)[2:]
        rightB = bin(right)[2:]
        
        # print leftB,rightB
        
        
        
        if(len(leftB)!=len(rightB)):
            return 0
        else:
            b='0b'
            i=0
            while(i<len(leftB) and leftB[i]==rightB[i]):
                b+=leftB[i]
                i+=1
            
            b+='0'*(len(leftB)-i)
            # print b,int(b,2)
            return int(b,2)
            
# way 2
class Solution(object):
    def rangeBitwiseAnd(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        """
        Observations:
            1. if any of ith bit  flips from 0 to 1 or 1 to 0 the ans ith bit will be  0 . as we are finding and
            2. if we are adding a new bit then all the right hand side bit are already flipped
                For example 2 & 3.   1 1.    1 0 0

            3. <---m bit (fixed - left and right bit will be equal)-----><-----n bit (flipped)----->
            
            
        
        """
    
        count=0
        while(left!=right):
            count+=1 # maintain the count of not flipped part
            left>>=1
            right>>=1# remove the not flipped part
        
        return left<<count

            