# Qus : https://leetcode.com/problems/permutations/

def solve(nums,out,a):
    if(nums==[]):
        out.append(a)
    #print nums,out,a
    for i in range(len(nums)):
        #take one element out of present elemnts in list
        #append in the a 
        #remove that elemnt from the given list so that next time we dont include
        #that elemnt again
        num2=[nums[j] for j in range(len(nums)) if j!=i]
        
        solve(num2,out,a+[nums[i]])
    

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        #brute force solution
        
        out=[]
        
        solve(nums,out,[])
        
        return out
    
    
        # SOl 2 
        # return list(itertools.permutations(nums,))


# solution editorial 2
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        out=[]
        n = len(nums)

        def recurse(permu,nums,n):

            if(len(permu)==n):
                out.append(permu[:])

            for i in range(len(nums)):

                temp = nums[:]
                permu.append(nums[i])
                nums = nums[:i]+nums[i+1:]
                recurse(permu,nums,n)
                permu.pop()
                nums = temp





        recurse([],nums,n)
        return out