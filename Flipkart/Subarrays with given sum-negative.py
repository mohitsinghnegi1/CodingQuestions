# Qus:https://practice.geeksforgeeks.org/problems/subarray-range-with-given-sum2804/1
#User function Template for python3
from collections import defaultdict
class Solution:
    def findSubarraySum(self,arr, n, Sum):  
        #code here
        
        d = defaultdict(int)
        d[0]=1
        
        prefixSum = 0
        count = 0
        
        for val in arr:
            prefixSum += val
            
            if(prefixSum - Sum in d):
                count += d[prefixSum - Sum]
            d[prefixSum]+=1
        return count
            
        
        
        
        
        
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3



t=int(input())
for _ in range(0,t):
    n=int(input())
    a=list(map(int,input().split()))
    s=int(input())
    ob = Solution()
    print(ob.findSubarraySum(a, n, s))
    
# } Driver Code Ends