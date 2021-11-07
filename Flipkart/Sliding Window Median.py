# Qus:https://leetcode.com/problems/sliding-window-median/
# need multiple revision


from heapq import heappush,heappop
from collections import defaultdict

class Solution(object):
    def medianSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[float]
        """
        
        if(k==1):
            return nums
        
        ans =[]
        lo = [] # max heap contains first 1/2 of min elemenents
        hi = []  # min heap contains element greater then  1/2 the min elements
        
        # always low will contains equal or more element than hi
        
        
        for i in range(k):
            
            if(i%2==0):
                # push to low
                if(hi!=[] and hi[0][0]<nums[i]):
                    no,index = heappop(hi)
                    heappush(lo,(-no,index))
                    heappush(hi,(nums[i],i))
                else:
                    heappush(lo,(-nums[i],i))
            else:
                # low always contains an element
                
                if(nums[i]<-lo[0][0]):
                    no,index = heappop(lo)
                    heappush(hi,(-no,index))
                    heappush(lo,(-nums[i],i))
                else:
                    heappush(hi,(nums[i],i))
        
        if(k%2):
            ans.append(-lo[0][0])
        else:
            ans.append((-lo[0][0]+hi[0][0])/2.0)
                    
        
        # print lo,hi,"before k"
        # first k is there now we need to add and remove an elemnt from a window
        # for that we need to have a to_remove dict 


        for i in range(k,len(nums)): # end of window , or the end number need to be inserted
            no_to_insert = nums[i]
            # we have our window clean

            # since the number of element remains constant so we just balance out the heaps
            # this will handle dublicate as well since we are not just removing but also adding the element
            # we need to find from where i need to delete the number to be remove then i need to insert a 
            # number in that heap as well

            no_to_remove = nums[i-k]
            
            
            if(no_to_insert>=hi[0][0]):
                
                heappush(hi,(no_to_insert,i))
                
                
                if(no_to_remove<=hi[0][0]):
                    no,index = heappop(hi)
                    heappush(lo,(-no,index))
                
            else:
                heappush(lo,(-no_to_insert,i))
                
                if(no_to_remove>=-lo[0][0]):
                    no,index = heappop(lo)
                    heappush(hi,(-no,index))
                
            # rectify the heaps
            # remove invalid ement if exist on top  bec later on we need to decide based on top element


            while(lo and lo[0][1]<=i-k):
                heappop(lo)

            while(hi and hi[0][1]<=i-k):
                heappop(hi)

            # print lo,hi
            if(k%2):
                ans.append(-lo[0][0])
            else:
                ans.append((-lo[0][0]+hi[0][0])/2.0)
        
        return ans
                    
                    
                
                
                
                
                
                
                
                    
                    
                
                
                
                
                
                
                
                
                
                
                
            
            
            
            
            
            
            
        
        