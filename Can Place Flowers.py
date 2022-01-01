# Qus:https://leetcode.com/problems/can-place-flowers/

class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        l = len(flowerbed)
        
        def canPlant(i,l):
            
        
            
            if(flowerbed[i]==1):
                return False
            
            if(i-1>=0 and flowerbed[i-1]==1):
                return False
            
            if(i+1<l and flowerbed[i+1]==1):
                return False
           
            
            return True
            
        d = {}
        
        def countPlant(i,n):
            
            
            
            if(i>=n):
                return 0
            
            
            if(d.get(i,False)!=False):
                return d[i]
            
            
            if(canPlant(i,n)):
                
                d[i] = 1 + countPlant(i+2,n)
                
                return d[i]
            
            d[i] = countPlant(i+1,n)
            
            return d[i]
        
        
        
        return countPlant(0,l)>=n
                
            
        
        
        
        
        
        
        