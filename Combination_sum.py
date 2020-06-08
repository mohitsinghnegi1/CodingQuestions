
# Qus:https://leetcode.com/problems/combination-sum/

def solve(candidates,target,result,start=0,out=[]):
    
    #if target becomes less then 0 means we can't add more number /can't add new number to creat a new
    #combination
    if(target<0):
        return 
    #if target==0 means this is a valid combination 
    if(target==0 ):
        result.append(out)
        return
    
    #we are looping through candidate array
    #if target is >=then 0 then more combinations are possible 
    for i in range(start,len(candidates)):
        if(target-candidates[i]<0):
            break
            
        #this will see any possible combination 
        solve(candidates,target-candidates[i],result,i,out+[candidates[i]])


class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        #we are sorting array to make qustion more efficient and easy
        candidates.sort()
        
        #this is the result array of array which contains unique combinations to make a target
        result=[]
        
        #this function will populate result with unique combination sum array
        solve(candidates,target,result)

        return result