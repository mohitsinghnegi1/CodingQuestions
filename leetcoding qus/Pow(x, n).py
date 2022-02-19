
# Qus : https://leetcode.com/problems/powx-n/

def power(x,n):
    if(d.get((x,n),False)):
        return d[(x,n)]
    
    #Dont forgot to handle negative case
    if(n<0):
        #notice below two conditions
        n=-n
        x=1/x
        
        
        d[(x,n/2)]=power(x,n/2)
        if(n%2==0):
            
            return d[(x,n/2)]*d[(x,n/2)]
        else:
            return d[(x,n/2)]*d[(x,n/2)]*x            

    if(n==0):
        d[(x,n)]=1
        return 1
    if(n==1):
        d[(x,n)]=x
        return x

    if(n%2==0):
            
        return d[(x,n/2)]*d[(x,n/2)]
    else:
        return d[(x,n/2)]*d[(x,n/2)]*x        

class Solution(object):
    
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        
        """
        global d
        d={}
        
        return pow(x,n)