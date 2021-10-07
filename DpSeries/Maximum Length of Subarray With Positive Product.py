# QUs:https://leetcode.com/problems/maximum-length-of-subarray-with-positive-product/

# Timecomplexity O(n)
# Space Complexity O(1)

def getMaxLength(nums,i):

    # i is starting of subarray
    j = i  # nums[i:j+1] will be the subarray we will be considering
    n = 0 # number of -ve numbers
    max1 = 0 # will store the ans for current subarray
    n_s = -1 # first -ve number in current subarray
    n_e = -1 # last -ve number index in current subarray

    while(j<len(nums) and nums[j]!=0): # break when we come to the end or if we encounter zero

        if(nums[j]<0):
            if(n_s==-1):n_s = j  # if first -ve is unset then set it
            n_e = j # update the last -ve
            n += 1 # increment the negaive


        if(n%2 == 0): # if number of -ve is even then we can update the length of i to j
            max1 = max(max1,j - i + 1)
        else: # case 2 with odd number of -ve
            max1 = max(max1,j - n_s ) # either [n_s+1:j] could be ans
            max1 = max(max1,n_e - i) # either [i:n_e] could be ans
            
        j+=1

    if(j+1<len(nums)-1):

        return max(max1,getMaxLength(nums,j+1)) # in case of zero we need to move to next subarray starting from i+1 
    
    return max1
    
    
class Solution(object):
    def getMaxLen(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
            Intution:
            
            case : If subarray contains even number of -ve
            then ans will be simply length of subarray
            
            case 2: If subarray contains odd number of -ve
                i) either we can remove prefix up to first -ve 
                ii) or we remove suffix starting from last -ve to end of subarray
            
            Edge case : We need to start our subarray again from i+1 if ith element is 0
            
        """
    
        return getMaxLength(nums,0)
        
        
        
        
            
            
            
            
        
        
        
        
        
        
        
        
        
        
        