def sqsum(n):
    sq=0
    while(n!=0):
        r=n%10
        sq+=r**2
        n/=10
    return sq
        
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        slow=sqsum(n)
        fast=sqsum(sqsum(n))
        # print slow,fast
        
        #point to note here is that fast and slow pointer will be equal eventually
        #if there is cycle the  they will meet at different number
        #if fast reaches to 1 it means we need to return True
        while(slow!=fast):
            
            slow=sqsum(slow)
            fast=sqsum(sqsum(fast))
            # print slow,fast
        if(slow==1):
            return True
        return False
            
            
        