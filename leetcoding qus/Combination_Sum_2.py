# Qus :https://leetcode.com/problems/combination-sum-ii/submissions/


def solve(candidates,target,result,start=0,out=[]):
    
    #if target becomes less then 0 means we can't add more number /can't add new number to creat a new
    #combination
    if(target<0 ):
        return 
    #if target==0 means this is a valid combination 
    if(target==0 ):
        result[tuple(out)]=True
        return
    
    #in case start > then number of candidates 
    if(start>=len(candidates)):
        return 
   
    #this will see any possible combination 
    
    solve(candidates,target-candidates[start],result,start+1,out+[candidates[start]])
    solve(candidates,target,result,start+1,out)



class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        #we are sorting array to make qustion more efficient and easy
        
        candidates.sort()
        
        #I am using dictionary here because it will prevent dublicates
        #dictionary contains tuples
        result={}
        
        #this function will populate result with unique combination sum array
        solve(candidates,target,result)
        
        res=[]
        for i in result:
            res.append(list(i))
            
        return res
            
            
        