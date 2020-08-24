# QUs:https://leetcode.com/problems/sliding-window-maximum/

# brute force solution
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if(len(nums)==0):
            return []
        #brute force
        out=[]
        for i in range(len(nums)-k+1):
            max1=-sys.maxsize
            for j in range(i,i+k):
                max1=max(nums[j],max1)
            out.append(max1)
        return out
                
#efficient solution

from collections import deque
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if(k<=1):
            return nums
        
        dq=deque()
        
        #push the candidate out element's index inside queue
        
        for i in range(k):
            
            while dq:
                if(nums[dq[-1]]<=nums[i]):
                    dq.pop()
                else:
                    break
            dq.append(i)
            
        out=[]
        print dq
        for i in range(k,len(nums)):
            out.append(nums[dq[0]])
            
            #check if left index in dequeu is still in range
            #if not pop left most index
            if(dq[0]<i-k+1):
                dq.popleft()
            
            while dq:
                #we need to compare value to pop out from the end of dq with the                     #current elemnt if current elemnt is greater then some of the                       #element in the dq then we will pop out those elemnet 
                if(nums[dq[-1]]<=nums[i]):
                    dq.pop()
                else:
                    break
            dq.append(i)
            
        #also append the max elemnt in last window
        out.append(nums[dq[0]])
        
        return out
            
        
        
        
        
        
        
        
        
        
        
        