# Qus:https://leetcode.com/problems/3sum/

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        #need to sort an array for better complexity , so that we can move in proper             #direction
        nums.sort()
        out=[]
        
        #keep first element fix and find other 2 
        #dont include duplicate elemnts
        #len(nums)-2 because we need triplet so need 2 places for other 2 number at least
        i=0
        while i<(len(nums)-2):
            #this is the target that we want to obtain from rest of two other element
            if(nums[i]>0):
                break
            target=-nums[i]
            
            left=i+1
            right=len(nums)-1
            
            while(left<right):
                
                sum1=nums[left]+nums[right]
                if(sum1<target):
                    left+=1
                elif(sum1>target):
                    right-=1
                else:
                    triplet=[nums[i],nums[left],nums[right]]
                    
                    out.append(triplet)
                    
                    #skip left dublicates
                    left+=1
                    while(left<right and nums[left]==triplet[1]):
                        left+=1
                    
                    #skip right dublicate
                    right-=1
                    while(right>left and nums[right]==triplet[2]):
                        right-=1
        
            i+=1
            #skip dublicate from first number
            while(i<len(nums) and nums[i]==nums[i-1]):
                    i+=1
        return out
            
                    
                    
                    
            
            
            
            
        
        