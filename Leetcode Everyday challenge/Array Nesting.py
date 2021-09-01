# Qus:https://leetcode.com/problems/array-nesting/

# TLE - N**2
class Solution(object):
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_so_far = 0
        for i in range(len(nums)):
            dict1 = {}
            j = i
            while(True):
                if(nums[j] not in dict1):
                    dict1[nums[j]] = True
                    j = nums[j]
                else:
                    max_so_far = max(max_so_far,len(dict1))
                    break
        return max_so_far
            
        
        # we can use dp
        # dp[i] = how far the set will go 


# using dp 
# accepted 16% faster
def dp(nums,i,visited,d):
    
    if(visited[i]==1):
        return 0
    if(d[i]!=0):
        return d[i]
    visited[i] = 1
    d[i] = 1+ dp(nums,nums[i],visited,d)
    return d[i]
    
class Solution(object):
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # we need to find the longest len of cyclic linked list
        max_so_far = 0
        d = [0]*len(nums)
        for i in range(len(nums)):
            visited = [0]*len(nums)
            max_so_far  = max(dp(nums,i,visited,d),max_so_far)
            
        return max_so_far


# improved by adding visited as gloabl , bec each loop element will be having same number of eleement in cycle
def dp(nums,i,visited,d):
    
    if(visited[i]==1):
        return 0
    if(d[i]!=0):
        return d[i]
    visited[i] = 1
    d[i] = 1+ dp(nums,nums[i],visited,d)
    return d[i]
    
class Solution(object):
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # we need to find the longest len of cyclic linked list
        max_so_far = 0
        d = [0]*len(nums)
        visited = [0]*len(nums)
        for i in range(len(nums)):
            if(visited[i]==0):
                max_so_far  = max(dp(nums,i,visited,d),max_so_far)
            
        return max_so_far


def dp(nums,i,visited):
    
    if(visited[i]==1):
        return 0
    visited[i] = 1
    return 1+ dp(nums,nums[i],visited)
    




class Solution(object):
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # we need to find the longest len of cyclic linked list
        max_so_far = 0
        visited = [0]*len(nums)
        for i in range(len(nums)):
            if(visited[i]==0):
                max_so_far  = max(dp(nums,i,visited),max_so_far)
            
        return max_so_far


# without dp 
def dp(nums,i,visited):
    
    if(visited[i]==1):
        return 0
    visited[i] = 1
    return 1+ dp(nums,nums[i],visited)
    

class Solution(object):
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # we need to find the longest len of cyclic linked list
        max_so_far = 0
        visited = [0]*len(nums)
        for i in range(len(nums)):
            if(visited[i]==0):
                max_so_far  = max(dp(nums,i,visited),max_so_far)
            
        return max_so_far

# iterative solution

class Solution(object):
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # we need to find the longest len of cyclic linked list
        max_so_far = 0
        visited = [0]*len(nums)
        for i in range(len(nums)):
            if(visited[i]==0):
                visited[i] = 1
                j = nums[i]
                count = 1
                while(j!=i):
                    visited[j] = 1
                    j = nums[j]
                    count += 1
                max_so_far  = max(count,max_so_far)
            
        return max_so_far


# we can further optimise space using the array itself